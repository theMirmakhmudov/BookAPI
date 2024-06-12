from fastapi import FastAPI
from db import users_db, book_db

app = FastAPI()


@app.get("/users/{user_id}")
async def get_users(user_id: int):
    return [user for user in users_db if user["id"] == user_id]


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    return [book for book in book_db if book["id"] == book_id]


@app.get("/booklist")
async def get_all_books():
    return book_db


@app.post("/books")
async def post_book_parameter(limit: int = 1, offset: int = 0):
    return book_db[offset:][:limit]
