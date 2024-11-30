# otomai

Rental management app: tenants, leases, payments

poetry run flask db migrate -m "Create contact table"

poetry run flask db upgrade

poetry run python seed.py

poetry run flask run --port=5001
