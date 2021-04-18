"""Store module."""
from db import db


class StoreModel(db.Model):
    """Store models class."""

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def json(self):
        """Convert to JSON."""
        # pylint: disable=E1101
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        """Find by name."""
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """Save to db."""
        # pylint: disable=E1101
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """Delete from db."""
        # pylint: disable=E1101
        db.session.delete(self)
        # pylint: disable=E1101
        db.session.commit()
