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
        return self.__get_note_by_id(id)

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
        note = self.__get_note_by_id(id)
        self.collections.remove(note)

    def __get_note_by_id(self, id: str):
        try:
            return list(filter(lambda x: x['id'] == id, self.collections))[0]
        except AttributeError as ae:
            print("Такой заметки не существует!")