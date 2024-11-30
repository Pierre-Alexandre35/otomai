from app.extensions import db


class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surface = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Rental id={self.id}, surface={self.surface}, rooms={self.rooms}, address={self.address}>"