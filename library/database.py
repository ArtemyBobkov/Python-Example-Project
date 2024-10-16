from library.member import Member


class LibraryDatabase:
    """Class representing an internal library database for managing members."""

    def __init__(self):
        # Create an empty dictionary to store members, keyed by name.
        # Private attribute is used to avoid accidental modificatio, marked as "_".
        self._members = {}

    def register_member(self, member: Member) -> None:
        """
        Register a member in the database.

        Args:
            member (Member): The member to register.

        Returns:
            None
        """
        if member.name in self._members:
            print(f"Member {member.name} is already registered.")
        else:
            self._members[member.name] = member
            print(f"Member {member.name} has been registered.")

    def is_member_registered(self, member: Member) -> bool:
        """
        Check if a member is registered.

        Args:
            member (Member): The member to check.

        Returns:
            bool: True if the member is already registered, False otherwise.
        """
        return member.name in self._members
