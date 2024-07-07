from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/print")
def print_demo():
    print('Hello')
    return {"Hello"}


@app.get("/{name}")
def print_demo():
    print('Hello')
    return {"Hello"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data == "bye":
            await websocket.send_text(f"接受到的消息是: {data}")
            await websocket.send_text("聊天关闭")
            await  websocket.close(100)
        else:
            await websocket.send_text(f"接受到的消息是: {data}")
