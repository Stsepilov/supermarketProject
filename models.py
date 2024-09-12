from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Groceries(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return (
            f"Patient(name='{self.name}', details='{self.details}', weight='{self.weight}', quantity='{self.quantity}'"
            f", price='{self.price}')")
