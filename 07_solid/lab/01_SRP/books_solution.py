class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'{self.title} from author {self.author} is on {self.page} page.'


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return 'Sorry, the book is not found.'

    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                del b


library = Library()
for num in range(1, 6):
    b = Book(f"Title {num}", f"Author {num}")
    if num == 3:
        b.turn_page(10)
    library.add_book(b)

print('\n'.join(str(book) for book in library.books))
