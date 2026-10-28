from app import Library

def test_add_and_view_books():
    lib = Library()
    lib.add_book("Test Book")
    books = lib.view_books()
    assert len(books) == 1
    assert books[0]["title"] == "Test Book"
    assert books[0]["available"] is True
