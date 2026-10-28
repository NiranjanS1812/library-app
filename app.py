class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = {"title": title, "available": True}
        self.books.append(book)
        return book

    def view_books(self):
        return self.books

if __name__ == "__main__":
    lib = Library()
    lib.add_book("Python Basics")
    print("Available Books:", lib.view_books())
