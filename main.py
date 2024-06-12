from fastapi import FastAPI
from db import users_db, book_db

app = FastAPI()


@app.get("/users/{user_id}")
async def get_users(user_id: int):
    return [user for user in users_db if user["id"] == user_id]


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    return [book for book in book_db if book["id"] == book_id]


@app.get("/books")
async def get_all_books():
    return book_db
