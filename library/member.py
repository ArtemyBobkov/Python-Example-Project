from dataclasses import dataclass

# Special decorator to automatically generate methods for the class, read the docs for more info
@dataclass 
class Member:
    """Class representing a library member."""
    
    name: str

    def __str__(self):
        """Return a string representation of the member."""
        return f"Member: {self.name}"

    def read_book(self, book):
        """Allow the member to read a book."""
        print(f"{self.name} is reading {book.title}.")