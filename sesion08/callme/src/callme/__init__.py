import asyncio
import time

from aiortc import RTCSessionDescription, RTCPeerConnection, MediaStreamTrack, MediaStreamError
from aiortc.contrib.media import MediaRelay
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fractions import Fraction

app = FastAPI()
relay = MediaRelay()

# kind -> audio o video

class Puente(MediaStreamTrack):
    def __init__(self, kind: str):
        super().__init__()
        self.kind = kind
        self.pista: MediaStreamTrack | None = None
        self.hay_pista = asyncio.Event()
        self.inicio = time.time()
        self.muestras = 0

    def conectar(self, pista: MediaStreamTrack):
        self.pista = pista
        self.hay_pista.set()

    def desconectar(self):
        self.pista = None
        self.hay_pista.clear()
    
    async def recv(self):
        while True:
            await self.hay_pista.wait()
            try:
                frame = await self.pista.recv()
                break
            except MediaStreamError:
                self.desconectar()

        if self.kind == "video":
            frame.pts = int((time.time() - self.inicio) * 90_000)
            frame.time_base = Fraction(1, 90_000)
        else:
            frame.pts = self.muestras
            frame.time_base = Fraction(1, frame.sample_rate)
            self.muestras += frame.samples
        return frame

class Participante:
    def __init__(self, ws: WebSocket, nombre: str):
        self.ws = ws
        self.nombre = nombre
        self.pc = RTCPeerConnection()
        self.mipista: dict[str, MediaStreamTrack] = {}
        self.invitadopista: dict[str, Puente] = { "audio": Puente("audio"), "video": Puente("video") }

    async def avisar(self, mensaje: dict):
        try:
            await self.ws.send_json(mensaje)
        except Exception:
            print("Se desconecto")


sala: list[Participante] = []

@app.websocket("/ws")
async def senalizacion(ws: WebSocket):
    await ws.accept()
    yo: Participante | None = None
    try:
        while True:
            msg = await ws.receive_json()

            if msg["tipo"] != "oferta" or yo is not None:
                continue

            if len(sala) >= 2:
                await ws.send_json({ "tipo": "llena" })
                await ws.close()
                return

            yo = Participante(ws=ws, nombre=msg["nombre"])
            otro: Participante | None = sala[0] if sala else None
            sala.append(yo)

            @yo.pc.on("track")
            def recibir_mis_pistas(pista: MediaStreamTrack):
                yo.mipista[pista.kind] = pista
                for participante in sala:
                    if participante is not yo:
                        participante.invitadopista[pista.kind].conectar(
                            relay.subscribe(pista)
                        )

            await yo.pc.setRemoteDescription(
                RTCSessionDescription(
                    sdp=msg["sdp"], type="offer"
                )
            )

            for pista in yo.invitadopista.values():
                yo.pc.addTrack(pista)
            
            if otro:
                for kind, pista in otro.mipista.items():
                    yo.invitadopista[kind].conectar(
                        relay.subscribe(pista)
                    )

            await yo.pc.setLocalDescription(
                await yo.pc.createAnswer()
            )

            await ws.send_json({
                "tipo": "respuesta",
                "sdp": yo.pc.localDescription.sdp,
            })

            if otro:
                await otro.avisar({
                    "tipo": "entro",
                    "nombre": yo.nombre,
                })
                await yo.avisar({
                    "tipo": "entro",
                    "nombre": otro.nombre,
                })
    except WebSocketDisconnect:
        pass
    finally:
        if yo:
            await salir(yo)

async def salir(yo: Participante):
    sala.remove(yo)
    for p in sala:
        for pista in p.invitadopista.values():
            pista.desconectar()
        await p.avisar({ "tipo": "salio", "nombre": yo.nombre })
    await yo.pc.close()
    print(f"{yo.nombre} salio de la sala")

app.mount("/", StaticFiles(directory="public", html=True))
