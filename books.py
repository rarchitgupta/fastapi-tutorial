from fastapi import FastAPI

books = {
    "book_1": {"title": "Book 1", "author": "Author 1"},
    "book_2": {"title": "Book 2", "author": "Author 2"},
    "book_3": {"title": "Book 3", "author": "Author 3"},
    "book_4": {"title": "Book 4", "author": "Author 4"},
    "book_5": {"title": "Book 5", "author": "Author 5"},
}

app = FastAPI()


@app.get("/")
async def read_all_books():
    return books


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "Favorite Book"}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id": book_id}
