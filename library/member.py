from dataclasses import dataclass
from library.books import Book


# Special decorator to automatically generate methods for the class, read the docs for more info
@dataclass
class Member:
    """Class representing a library member."""

    name: str

    def __str__(self):
        """Return a string representation of the member."""
        return f"Member: {self.name}"

    def read_book(self, book: Book) -> None:
        """
        Allow the member to read a book.

        Args:
            book (Book): The book to read.

        Returns:
            None
        """
        print(f"{self.name} is reading {book.title}.")
