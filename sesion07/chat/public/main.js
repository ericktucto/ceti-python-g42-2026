let token = null
const HOST = location.host
const SSL = location.protocol.includes("https")
const JWT = true

/**
 * Realtime: abstrae socket.io o WebSocket nativo (ws) del navegador.
 * Expone los mismos métodos on(evento, cb) y send(evento, data)
 * sin importar el transporte que se use por debajo.
 */
class Realtime {
    /**
     * @param {string} url  URL del servidor.
     * @param {"socketio"|"ws"} driver  Transporte a usar.
     */
    constructor(url, driver = "ws") {
        this.url = url;
        this.driver = driver;
        this.listeners = {}; // { evento: [cb, cb, ...] }
        this.socket = null;

        if (driver === "socketio") {
            this._initSocketIO();
        } else {
            this._initWS();
        }
    }

    // --- socket.io ---
    _initSocketIO() {
        // Requiere haber cargado el cliente de socket.io (window.io).
        this.socket = window.io(this.url, {
            auth: { token }
        });
        this.socket.onAny((event, data) => {
            this._emit(event, data)
        });
    }

    // --- WebSocket nativo ---
    _initWS() {
        this.socket = new WebSocket(this.url);
        this.socket.addEventListener("message", (msg) => {
            try {
                const { event, data } = JSON.parse(msg.data);
                this._emit(event, data);
            } catch (e) {
                // mensaje no válido, se ignora
            }
        });
    }

    /** Escuchar un evento. */
    on(event, cb) {
        if (!this.listeners[event]) this.listeners[event] = [];
        this.listeners[event].push(cb);
    }

    /** Enviar un evento con datos. */
    send(event, data) {
        if (this.driver === "socketio") {
            this.socket.emit(event, data);
        } else {
            // El WebSocket puede no estar abierto todavía.
            const payload = JSON.stringify({ event, data });
            if (this.socket.readyState === WebSocket.OPEN) {
                this.socket.send(payload);
            } else {
                this.socket.addEventListener("open", () => this.socket.send(payload), { once: true });
            }
        }
    }

    /** Dispara internamente los callbacks registrados. */
    _emit(event, data) {
        (this.listeners[event] || []).forEach((cb) => cb(data));
    }
}

/* ------------------------------------------------------------------ */
/* UI del chat                                                         */
/* ------------------------------------------------------------------ */

// Elementos
const loginCard = document.getElementById("login-card");
const inputEmail = document.getElementById("email");
const inputPassword = document.getElementById("password");
const btnLogin = document.getElementById("login-btn");

const joinCard = document.getElementById("join-card");
const chatCard = document.getElementById("chat-card");
const roomInput = document.getElementById("room");
const usernameInput = document.getElementById("username");
const joinBtn = document.getElementById("join-btn");
const leaveBtn = document.getElementById("leave-btn");
const chatRoom = document.getElementById("chat-room");
const messagesEl = document.getElementById("messages");
const typingEl = document.getElementById("typing");
const messageInput = document.getElementById("message");
const sendBtn = document.getElementById("send-btn");

// Estado
let rt = null;
let myId = null;
let username = "";
let room = "";
let typingUsers = []; // array de ids que están escribiendo
let typingTimeout = null;

document.addEventListener('DOMContentLoaded', () => {
    if (JWT) {
        loginCard.classList.remove('hidden');
    } else {
        joinCard.classList.remove('hidden');
    }
})

/* ---------------------- Unirse a la sala -------------------------- */
btnLogin.addEventListener("click", async () => {
    const email = inputEmail.value
    const password = inputPassword.value

    const protocol = SSL ? "https" : "http";
    fetch(`${protocol}://${HOST}/api/auth/login`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify({ email, password })
    }).then(d.json())
    .then(data => {
        console.log("Hola")
        token = data.token

        loginCard.classList.add('hidden')
        joinCard.classList.remove('hidden')
    }).catch((e) => {
        console.log("hola mundo")
        console.error(e)
    })
})

/* ---------------------- Unirse a la sala -------------------------- */
joinBtn.addEventListener("click", () => {
    room = roomInput.value.trim();
    username = usernameInput.value.trim();
    if (!room || !username) return;

    // Cambia la URL / driver según tu backend.
    // ws:  new Realtime("ws://localhost:3000", "ws")
    // io:  new Realtime("http://localhost:3000", "socketio")
    const protocol = SSL ? "wss" : "ws";
    rt = new Realtime(`${protocol}://${HOST}`, "socketio");

    registerEvents();

    rt.send("join", { room, username });

    chatRoom.textContent = "# " + room;
    joinCard.classList.add("hidden");
    chatCard.classList.remove("hidden");
});

/* ------------------------ Eventos Realtime ------------------------ */
function registerEvents() {
    // El servidor nos asigna un id al unirnos.
    rt.on("joined", (data) => {
        myId = data.id;
        chatRoom.textContent = "# " + room + ` (${username})`;
    });

    rt.on("new-user", (data) => {
        newUser(data.username)
    });

    rt.on("leave-user", (data) => {
        leaveUser(data.username)
    });

    // Mensaje nuevo: { id, username, text }
    rt.on("message", (data) => {
        addMessage(data);
    });

    // Typing: { id, typing } -> true empieza, false deja de escribir
    rt.on("typing", (data) => {
        updateTyping(data.id, data.name, data.typing);
    });
}

/* ------------------------- Enviar mensaje ------------------------- */
function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;

    rt.send("message", { room, username, text });

    // También lo pintamos localmente como mío.
    addMessage({ id: myId, username, text }, true);

    messageInput.value = "";
    rt.send("typing", { room, name: username, typing: false });
}

sendBtn.addEventListener("click", sendMessage);
messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
});

/* --------------------- Emitir evento typing ----------------------- */
messageInput.addEventListener("input", () => {
    rt.send("typing", { room, name: username, typing: true });

    clearTimeout(typingTimeout);
    typingTimeout = setTimeout(() => {
        rt.send("typing", { room, typing: false });
    }, 1500);
});

/* ------------------------- Pintar mensaje ------------------------- */
function addMessage(data, mine = false) {
    const bubble = document.createElement("div");
    bubble.classList.add("bubble", mine ? "bubble--mine" : "bubble--other");

    if (!mine) {
        const author = document.createElement("span");
        author.classList.add("bubble__author");
        author.textContent = data.username || data.id;
        bubble.appendChild(author);
    }

    bubble.appendChild(document.createTextNode(data.text));
    messagesEl.appendChild(bubble);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

/* ------------------------- Llegada de un nuevo usuario ------------------------- */
function newUser(username) {
    const bubble = document.createElement("div");
    bubble.classList.add("bubble--new-user");

    bubble.appendChild(document.createTextNode(username + " se unió al chat"));
    messagesEl.appendChild(bubble);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

/* ------------------------- Un usuario deja el chat ------------------------- */
function leaveUser(username) {
    const bubble = document.createElement("div");
    bubble.classList.add("bubble--new-user");

    bubble.appendChild(document.createTextNode(username + " dejó el chat"));
    messagesEl.appendChild(bubble);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

/* --------------- Manejo del array de "escribiendo" ---------------- */
function updateTyping(id, name, isTyping) {
    if (id === myId) return; // no me muestro a mí mismo

    const idx = typingUsers.indexOf(id);
    if (isTyping && idx === -1) {
        typingUsers.push(id);
    } else if (!isTyping && idx !== -1) {
        typingUsers.splice(idx, 1);
    }

    renderTyping(name);
}

function renderTyping(name) {
    if (typingUsers.length === 0) {
        typingEl.textContent = "";
    } else if (typingUsers.length === 1) {
        typingEl.textContent = `${name} está escribiendo...`;
    } else {
        typingEl.textContent = `${typingUsers.join(", ")} están escribiendo...`;
    }
}

/* ----------------------------- Salir ------------------------------ */
leaveBtn.addEventListener("click", () => {
    if (rt) rt.send("leave", { room, username });

    typingUsers = [];
    messagesEl.innerHTML = "";
    typingEl.textContent = "";

    chatCard.classList.add("hidden");
    if (JWT) {
        loginCard.classList.remove("hidden");
    } else {
        joinCard.classList.remove('hidden')
    }
});
