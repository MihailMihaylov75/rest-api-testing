__author__ = "Mihail Mihaylov"

import unittest

from tests.test_base import TestBase

# from models.item import ItemModel


class ItemTest(TestBase):
    def test_crud(self):
        with self.app.app_context():
            pass
            # item = ItemModel("test", 19.99)
            # Check does not exist in database
            # self.assertIsNone(ItemModel.find_by_name("test"))
            # Add to database
            # item.save_to_db()
            # Check exist in database
            # self.assertIsNotNone(ItemModel.find_by_name("test"))


if __name__ == "__main__":
    unittest.main()
