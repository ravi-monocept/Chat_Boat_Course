from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import json

app = FastAPI()

book_dict = [
    {"title": "Title one", "author": "Author One", "category": "science"},
    {"title": "Title two", "author": "Author two", "category": "physics"},
    {"title": "Title three", "author": "Author three", "category": "biology"},
    {"title": "Title four", "author": "Author four", "category": "chesmetry"},
    {"title": "Title five", "author": "Author six", "category": "science"},
    {"title": "Title six", "author": "Author six", "category": "ccc"},
]


class Book(BaseModel):
    title: str
    author: str
    category: str


BOOKS = [Book(**data) for data in book_dict]


@app.get("/books")
async def read_All_books():
    return BOOKS


@app.get("/books/mybook")
async def read_all_books():
    return {"book_title": "my favourate book !"}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.title.casefold() == book_title.casefold():
            return book
    return {"Unable to find Book with title ": book_title}


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.title.casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book: Book):
    BOOKS.append(new_book)
    return "Book created !"


@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i in range(len(BOOKS)):
        if BOOKS[i].title.casefold() == updated_book.title.casefold():
            BOOKS[i] = updated_book
            return "Update completed"


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].title.casefold() == book_title.casefold():
            BOOKS.pop(i)
            return f"Book with {book_title} deleted successfully !"


# Assignment

# Here is your opportunity to keep learning!

# 1. Create a new API Endpoint that can fetch all books from a specific author
# using either Path Parameters or Query Parameters.


# Solution in next video
@app.get("/booksauthor")
async def read_author_by_query(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.author.casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return
