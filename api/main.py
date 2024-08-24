from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def ping_pong():
    return "ping pong2"
