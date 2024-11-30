from app.extensions import db


class Tenant(db.Model):
    __tablename__ = "tenant"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)

    # Use string "rental.id" for the ForeignKey reference
    rental_id = db.Column(db.Integer, db.ForeignKey("rental.id"), unique=True)
    rental = db.relationship("Rental", back_populates="tenant")

    def __repr__(self):
        return f"<Tenant id={self.id}, first_name={self.first_name}, last_name={self.last_name}>"
