# Appointments Pro

A Django backend prototype for business appointment management.

## Domain models
- Businesses and services, including service duration and price.
- Time slots with availability status.
- Customers and appointments with pending, confirmed and canceled states.
- Payment records with amount, status and transaction reference.

## Structure
- `business/`: business and service models, serializers and views.
- `appointments/`: scheduling models, serializers and views.
- `payments/`: payment record models.
- `setup/`: Django configuration.

## Status
Work in progress. Payment records do not establish a working payment gateway integration. A complete installation workflow and runtime tests have not been verified.
