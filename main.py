import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Full detail model for a book
class Book(BaseModel):
    id: int
    title: str
    author: str
    summary: str

@app.get("/item", summary="Get a single book")
async def get_book() -> Book:
    """
    Returns a single book with full details.
    """
    return Book(
        id=1,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        summary="A story of the mysteriously wealthy Jay Gatsby and his love for Daisy Buchanan."
    )

@app.get("/items", summary="Get list of books")
async def get_books() -> List[Book]:
    """
    Returns a list of books with full details.
    """
    return [
        Book(
            id=1,
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            summary="A story of the mysteriously wealthy Jay Gatsby and his love for Daisy Buchanan."
        ),
        Book(
            id=2,
            title="1984",
            author="George Orwell",
            summary="A dystopian novel set in a totalitarian society."
        ),
        Book(
            id=3,
            title="To Kill a Mockingbird",
            author="Harper Lee",
            summary="A novel about racial injustice in the Deep South."
        )
    ]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
