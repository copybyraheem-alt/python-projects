class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    def get_info(self):
        return f"'{self.title}' by {self.author}"

    @classmethod
    def from_string(cls, book_str):
        if "-" not in book_str:
            raise ValueError("Input string must contain '-' separating title and author")
        var1, var2 = book_str.rsplit("-", 1)
        title = var1.strip()
        author = var2.strip()
        if not title or not author:
            raise ValueError("Both title and author must be non-empty")
        return cls(title, author)

    @classmethod
    def get_total_books(cls):
        return cls.total_books


if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book.from_string("Dune-Frank Herbert")

    print(book1.get_info())
    print(book2.get_info())
    print(Book.get_total_books())
