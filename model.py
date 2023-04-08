"""This is the model module.

Manages the collection of notes.
"""


class Notes:
    """
    Class for working with a collection of notes.
    """

    def __init__(self, data: list):
        self.collections = data

    def __str__(self):
        return f"Notes: {self.collections}"

    def __repr__(self):
        return f"Notes({self.collections})"

    def get_notes(self) -> list:
        """
        Get collections of notes.

        :return: list
        """
        return self.collections

    def add(self, note: dict) -> None:
        """
        Add the note to collection.

        :param note: dict. Note object.
        :return: None
        """
        self.collections.append(note)

    def read(self, id: str) -> dict:
        """
        Read the note from collection.

        :param id: str. Note id.
        :return: dict
        """
        print("Прочли")

    def edit(self, **kwargs) -> None:
        """
        Edit the note from collection.

        :param kwargs: Can be id, tittle, msg.
        :return: None
        """
        print("Обновили")

    def delete(self, id: str) -> None:
        """
        Delete the note from collection.

        :param id: str. Note id.
        :return: None
        """
        print("Удалили")
