from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            listing = Listing.objects.create(
                listing_id=fake.uuid4(),
                host_id=fake.uuid4(),
                name=fake.company(),
                description=fake.text(max_nb_chars=200),
                location=fake.city(),
                pricepernight=round(random.uniform(50.0, 500.0), 2),
                created_at=fake.date_time_this_decade(),
                updated_at=fake.date_time_this_decade()
            )
