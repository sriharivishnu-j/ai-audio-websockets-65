import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.services.audio_analysis import analyze_audio
from app.utils.logger import setup_logging

setup_logging()
app = FastAPI()

@app.websocket("/ws/audio")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            result = analyze_audio(data)
            await websocket.send_text(result)
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)