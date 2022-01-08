from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(
        title="Description of the Book", max_length=100, min_length=1
    )
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "de970e77-efcb-430a-ab5d-dad9f61de33b",
                "title": "Animal Farm",
                "author": "George Orwell",
                "description": "Animal rebellion against humans",
                "rating": 85,
            }
        }


app = FastAPI()

books = []


@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if books_to_return and len(books) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(books[i - 1])
            i += 1
        return new_books
    return books


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise item_cannot_be_found_exception()


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in books:
        counter += 1
        if x.id == book_id:
            books[counter - 1] = book
            return books[counter - 1]
    raise item_cannot_be_found_exception()


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for x in books:
        counter += 1
        if x.id == book_id:
            del books[counter - 1]
            return f"ID: {book_id} deleted"
    raise item_cannot_be_found_exception()


@app.post("/")
async def create_book(book: Book):
    books.append(book)
    return book


def item_cannot_be_found_exception():
    return HTTPException(
        status=404,
        detail="Book not found",
        headers={"X-Header-Error": "Nothing to be seen at UUID"},
    )
