from app.extensions import db


class Tenant(db.Model):
    __tablename__ = "tenant"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)

    # Link to Rental
    rental_id = db.Column(db.Integer, db.ForeignKey("rental.id"), unique=True)
    rental = db.relationship("Rental", back_populates="tenant")

    # Link to User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="tenants")

    # New column to store GCS path
    gcs_path = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return (
            f"<Tenant id={self.id}, first_name={self.first_name}, "
            f"last_name={self.last_name}, gcs_path={self.gcs_path}>"
        )
