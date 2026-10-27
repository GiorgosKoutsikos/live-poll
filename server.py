from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

active_connections = []

poll_data = {
  "Python": 0,
  "JavaScript": 0,
  "Go": 0
}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    await websocket.send_json(poll_data)

    try:
        while True:
          option = await websocket.receive_text()
          if option in poll_data:
            poll_data[option] += 1

          for connection in active_connections:
            await connection.send_json(poll_data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open ("index.html", "r", encoding="utf-8") as f:
      text  = f.read()
    return text
