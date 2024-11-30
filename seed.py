from app import create_app
from app.extensions import db
from app.models.rentals import Rental

app = create_app()

with app.app_context():
    # Add rental data
    db.session.add_all(
        [
            Rental(surface=50, rooms=2, address="123 Main Street"),
            Rental(surface=75, rooms=3, address="456 Elm Street"),
            Rental(surface=100, rooms=4, address="789 Oak Avenue"),
        ]
    )
    db.session.commit()
    print("Rental database seeded!")
