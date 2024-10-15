from library.member import Member

class LibraryDatabase:
    """Class representing an internal library database for managing members."""
    
    def __init__(self):
        self._members = {}

    def register_member(self, member: Member):
        """Register a member in the database."""
        if member.name in self._members:
            print(f"Member {member.name} is already registered.")
        else:
            self._members[member.name] = member
            print(f"Member {member.name} has been registered.")

    def is_member_registered(self, member: Member) -> bool:
        """Check if a member is registered."""
        return member.name in self._members