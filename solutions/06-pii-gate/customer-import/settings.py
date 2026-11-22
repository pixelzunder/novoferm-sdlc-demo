"""Settings for the customer import. Secrets come from the environment."""

import os

PRICING_API_URL = "https://pricing.example.com/v1"
PRICING_API_KEY = os.environ["PRICING_API_KEY"]
DB_USER = "import"
DB_PASSWORD = os.environ["DB_PASSWORD"]
