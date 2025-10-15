from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "fastapi is working"}

@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"hi {name}" }