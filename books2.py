from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(
        title="Description of the Book", max_length=100, min_length=1
    )
    rating: int


app = FastAPI()

books = []


@app.get("/")
async def read_all_books():
    return books


@app.post("/")
async def create_book(book: Book):
    books.append(book)
    return book
