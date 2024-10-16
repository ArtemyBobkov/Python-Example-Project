from library import Book, DigitalBook, AudioBook, Member
from library.database import LibraryDatabase
from utils.helper import display_welcome_message


def run_library_system():
    """Run the library system simulation."""
    display_welcome_message()

    # Create a library database
    library_db = LibraryDatabase()

    # Create a member instance and register
    member = Member("John Doe")
    library_db.register_member(member)

    # Create book instances
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    digital_book = DigitalBook("1984", "George Orwell", "PDF")
    audio_book = AudioBook("To Kill a Mockingbird", "Harper Lee", "10 hours")

    # Demonstrate polymorphism
    for item in [book, digital_book, audio_book]:
        print(item.get_description())

    # Allow the member to read books if registered
    if library_db.is_member_registered(member):
        member.read_book(book)
        member.read_book(digital_book)
