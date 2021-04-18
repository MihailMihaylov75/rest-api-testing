import unittest
from models.item import ItemModel


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self.item = ItemModel("test", 19.99)

    def tearDown(self) -> None:
        del self.item

    def test_create_item(self):
        self.assertEqual(self.item.name, "test")
        self.assertEqual(self.item.price, 19.99)

    def test_json_item(self):
        expected = {"name": "test", "price": 19.99}
        self.assertEqual(self.item.json(), expected)


if __name__ == "__main__":
    unittest.main()
