"""Item module."""
from db import db


class ItemModel(db.Model):
    """ItemModel class."""

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        """Convert to JSON."""
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        """Find by name."""
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """Save to db."""
        # pylint: disable=E1101
        db.session.add(self)
        # pylint: disable=E1101
        db.session.commit()

    def delete_from_db(self):
        """Delete from db."""
        # pylint: disable=E1101
        db.session.delete(self)
        # pylint: disable=E1101
        db.session.commit()
