from dotenv import load_dotenv
load_dotenv()

import socketio
from fastapi import FastAPI
from chat.routers import auth

# servidor websockets
sio = socketio.AsyncServer(async_mode="asgi")

# servidor http
api = FastAPI()
api.frontend('/', directory='public')

# AUTH
api.include_router(router=auth.router)

app = socketio.ASGIApp(sio, api)

@sio.event
async def connect(sid: str, environ, auth):
    token = auth['token']
    print("-" * 15, "conectado", sid, token)


@sio.on('join')
async def unirse(sid: str, datos):
    room = datos['room']
    username = datos['username']

    await sio.save_session(sid, {
        "room": room,
        "username": username,
    })

    await sio.enter_room(sid, room)
    await sio.emit('new-user', data={
        "id": sid,
        "username": username,
    }, room=room, skip_sid=sid)

@sio.on('message')
async def mensaje(sid: str, datos):
    session = await sio.get_session(sid)
    room = session['room']
    username = session['username']

    await sio.emit('message', data={
        "id": sid,
        "room": room,
        "username": username,
        "text": datos['text'],
    }, room=room, skip_sid=sid)

@sio.on('typing')
async def tipiando(sid: str, datos):
    session = await sio.get_session(sid)
    room = session['room']
    username = session['username']

    await sio.emit('typing', data={
        "id": sid,
        "name": username,
        "typing": datos['typing'],
    }, room=room, skip_sid=sid)

