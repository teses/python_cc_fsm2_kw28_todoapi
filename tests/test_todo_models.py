import unittest

from pydantic import ValidationError
from models.todo import ToDoCreate

class TestToDoModels(unittest.TestCase):


    def test_todo_create(self):

        todo = ToDoCreate(
            todo_title="Python",
            todo_description="Hallo"
        )

        self.assertEqual(todo.todo_title, "Python")
        self.assertEqual(todo.todo_description, "Hallo")


    def test_todo_create_empty_title(self):

        # try:
        #     todo = ToDoCreate(
        #         todo_title="",
        #         todo_description="Hallo",
        #     )
        # except ValidationError as e:
        #     print(e)

        # wenn ein Fehler kommt ist es richtig
        with self.assertRaises(ValidationError):
            todo = ToDoCreate(todo_title="", todo_description="Hallo")


if __name__ == "__main__":
    unittest.main()

