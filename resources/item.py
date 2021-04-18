"""Item module."""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    """Item class."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store id."
    )

    # pylint: disable=R0201
    @jwt_required()
    def get(self, name):
        """Get item."""
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    # pylint: disable=R0201
    def post(self, name):
        """Post item."""
        if ItemModel.find_by_name(name):
            return (
                {"message": "An item with name '{}' already exists.".format(name)},
                400,
            )

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        # pylint: disable=W0702
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    # pylint: disable=R0201
    def delete(self, name):
        """Delete item."""
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "Item deleted"}

    # pylint: disable=R0201
    def put(self, name):
        """Put item."""
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    """Item list class."""

    # pylint: disable=R0201
    def get(self):
        """Get list of items."""
        return {"items": [x.json() for x in ItemModel.query.all()]}
