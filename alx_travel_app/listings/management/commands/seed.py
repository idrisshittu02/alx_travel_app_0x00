from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.company(),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(50.0, 500.0), 2),
                available=fake.boolean()
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

            # booking = Booking.objects.create(
            #     title=fake.sentence(nb_words=6),
            #     description=fake.text(),
            #     location=fake.city(),
            #     price=fake.random_number(digits=5, fix_len=True) / 100,
            #     available=fake.boolean()
            # )
            # self.stdout.write(self.style.SUCCESS(f'Created booking: {booking.title}'))

            # Review.objects.create(
            #     listing=listing,
            #     reviewer_name=fake.name(),
            #     reviewer_email=fake.email(),
            #     rating=fake.random_int(min=1, max=5),
            #     comment=fake.text()
            # )
            # self.stdout.write(self.style.SUCCESS(f'Created review for listing: {listing.title}'))