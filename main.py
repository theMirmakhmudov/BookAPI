from fastapi import FastAPI, HTTPException
from models import Book

app = FastAPI()

data = {
    "id": 1,
    "user_id": 1,
    "title": "Hello world fastapi",
    "body": "My first fastapi build book api"
}


@app.get("/")
async def book():
    return {"name": "Hello world"}


@app.get("/item/{item_id}")
async def items(item_id: int):
    return {"item_id": item_id}


@app.get("/name/{name}")
async def items(name: str):
    if name.isnumeric():
        type_hint = int()
        raise HTTPException(status_code=404, detail=f"Type Error ({type_hint})")
    return {"name": name}


@app.get("/book")
async def dates():
    return data


@app.post("/create")
async def book_create(book: Book):
    return {"book": book}
