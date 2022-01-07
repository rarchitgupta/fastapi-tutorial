from fastapi import FastAPI
from typing import Optional
from enum import Enum

books = {
    "book_1": {"title": "Book 1", "author": "Author 1"},
    "book_2": {"title": "Book 2", "author": "Author 2"},
    "book_3": {"title": "Book 3", "author": "Author 3"},
    "book_4": {"title": "Book 4", "author": "Author 4"},
    "book_5": {"title": "Book 5", "author": "Author 5"},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


app = FastAPI()


@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = books.copy()
        del new_books[skip_book]
        return new_books
    return books


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0

    if len(books) > 0:
        for book in books:
            x = int(book.split("_")[-1])
            if x > current_book_id:
                current_book_id = x
    books[f"book_{current_book_id+1}"] = {"title": book_title, "author": book_author}
    return books[f"book_{current_book_id+1}"]


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {"title": book_title, "author": book_author}
    books[book_name] = book_information
    return book_information


@app.delete("/{book_name}")
async def delete_book(book_name):
    del books[book_name]
    return f"{book_name} deleted."


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "Favorite Book"}


@app.get("/{book_name}")
async def read_book(book_name: str):
    return books[book_name]


@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "Right"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}
