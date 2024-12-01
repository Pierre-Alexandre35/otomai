from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.rentals import Rental
from app.models.tenants import Tenant

app = create_app()

with app.app_context():
    # Create users
    users = [
        User(email="user1@example.com"),
        User(email="user2@example.com"),
    ]
    users[0].set_password("password1")
    users[1].set_password("password2")
    db.session.add_all(users)
    db.session.commit()

    # Add rental data
    rentals = [
        Rental(surface=50, rooms=2, address="123 Main Street"),
        Rental(surface=75, rooms=3, address="456 Elm Street"),
        Rental(surface=100, rooms=4, address="789 Oak Avenue"),
    ]
    db.session.add_all(rentals)
    db.session.commit()

    # Add tenant data linked to rentals and users
    tenants = [
        Tenant(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            rental=rentals[0],
            user=users[0],  # Assign to user1
        ),
        Tenant(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            rental=rentals[1],
            user=users[0],  # Assign to user1
        ),
        Tenant(
            first_name="Alice",
            last_name="Brown",
            email="alice.brown@example.com",
            rental=rentals[2],
            user=users[1],  # Assign to user2
        ),
    ]
    db.session.add_all(tenants)
    db.session.commit()

    print("Users, Rentals, and Tenants database seeded!")
