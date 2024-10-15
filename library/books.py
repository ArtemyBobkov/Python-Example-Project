from dataclasses import dataclass

# As you see, we can write several classes in a single file if they are related and simple
@dataclass
class Book:
    """Class representing a physical book."""
    
    title: str
    author: str

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

    def get_description(self):
        """Return a description of the book."""
        return f"{self.title} is a book written by {self.author}."


@dataclass
class DigitalBook(Book):
    """Class representing a digital book, inheriting from Book."""
    
    format: str

    def __str__(self):
        """Return a string representation of the digital book."""
        return f"Digital Book: {self.title} by {self.author} in {self.format} format"

    def get_description(self):
        """Return a description of the digital book."""
        return f"{self.title} is a digital book in {self.format} format, written by {self.author}."


@dataclass
class AudioBook(Book):
    """Class representing an audio book, inheriting from Book."""
    
    duration: str

    def __str__(self):
        """Return a string representation of the audio book."""
        return f"Audio Book: {self.title} by {self.author}, duration {self.duration}"

    def get_description(self):
        """Return a description of the audio book."""
        return f"{self.title} is an audio book with a duration of {self.duration}, written by {self.author}."