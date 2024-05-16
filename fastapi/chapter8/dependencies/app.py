import asyncio
from datetime import datetime
from typing import Optional
from fastapi import Cookie, FastAPI, WebSocket, status
from starlette.websockets import WebSocketDisconnect

API_TOKEN = "SECRET_API_TOKEN"

app = FastAPI()

async def echo_message(websocket: WebSocket):
    data = await websocket.receive_text()
    await websocket.send_text(f"Message text was: {data}")

async def send_time(websocket: WebSocket):
    await asyncio.sleep(10)
    await websocket.send_text(f"It is: {datetime.utcnow().isoformat()}")


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str = "Anonymous",
    token: Optional[str] = Cookie(None),
):
    print(token)
    if token != API_TOKEN:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    await websocket.accept()
    await websocket.send_text(f"Hello, {username}!")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"{username}: {data}")
    except WebSocketDisconnect:
        await websocket.close()