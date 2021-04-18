"""Resources store module."""
from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    """Store models class."""

    # pylint: disable=R0201
    def get(self, name):
        """Get resource."""
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    # pylint: disable=R0201
    def post(self, name):
        """Post resource."""
        if StoreModel.find_by_name(name):
            return (
                {"message": "A store with name '{}' already exists.".format(name)},
                400,
            )

        store = StoreModel(name)
        try:
            store.save_to_db()
        # pylint: disable=W0702
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        """Delete resource."""
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {"message": "Store deleted"}


class StoreList(Resource):
    """StoreList class."""

    # pylint: disable=R0201
    def get(self):
        """Get list of stores."""
        return {"stores": [store.json() for store in StoreModel.query.all()]}
