# otomai

Rental management app: tenants, leases, payments

## Run the application

- Requirements: poetry and Python3
  `poetry install`
  `poetry run flask run --port=5001`

## Update a model

- Step 1: update your model within `app/models`
- Step 2: `poetry run flask db migrate --autogenerate -m "Create contact table" `
- Step 3: apply changes using `poetry run flask db upgrade`

Optional: insert seed data using `poetry run python seed.py`

## Todo

```
gcloud compute firewall-rules create allow-ssh \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:22 \
    --source-ranges=0.0.0.0/0

gcloud compute instances add-metadata postgres-instance \
    --metadata serial-port-enable=1 --zone=europe-west9-b

```
