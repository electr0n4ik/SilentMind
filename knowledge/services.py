import random

import stripe
from django.conf import settings


def gen_random_num() -> str:
    return ''.join(str(random.randint(1, 9)) for _ in range(8))


def create_price():
    stripe.api_key = settings.SECRET_KEY_STRIPE

    starter_subscription = stripe.Product.create(
        name="Starter Subscription",
        description="$12/Month subscription",
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=1200,
        currency="usd",
        recurring={"interval": "month"},
        product=starter_subscription['id'],
    )

    # Save these identifiers
    print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
    print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")
