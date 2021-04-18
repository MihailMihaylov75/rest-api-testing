import unittest
from models.item import ItemModel
from tests.test_base import TestBase


class TestItem(TestBase):
    def test_crud(self):
        with self.app.app_context():
            item = ItemModel("test", 19.99, 1)

            self.assertIsNone(
                ItemModel.find_by_name("test"),
                "Found an item with name {}, but expected not to.".format(item.name),
            )

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name("test"))

            item.delete_from_db()


if __name__ == "__main__":
    unittest.main()
