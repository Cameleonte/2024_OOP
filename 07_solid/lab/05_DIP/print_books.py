from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):

    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter(BaseFormatter):

    def format(self, book: Book) -> str:
        return book.content


class FacebookFormatter(BaseFormatter):

    def format(self, book: Book) -> str:
        return book.content[:5]


class Printer:

    def get_book(self, book: Book, formatter: BaseFormatter):
        formatted_book = formatter.format(book)
        return formatted_book


book = Book('My enormous, huge, giant book!')
prin = Printer()
print(prin.get_book(book, FacebookFormatter()))
