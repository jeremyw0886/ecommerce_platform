# Used for seeding the database with fake products. This is useful for testing purposes. The command creates a category named Electronics and then creates 10 fake products under that category. The products have random names, descriptions, prices, stock, and availability. The image field is set to a placeholder image. The command can be run using the following command:


import random

from django.core.management.base import BaseCommand
from faker import Faker

from store.models import Category, Product


class Command(BaseCommand):
    help = "Seed the database with fake products"

    def handle(self, *args, **options):
        fake = Faker()
        # Create or get a category
        category, created = Category.objects.get_or_create(
            name="Electronics", slug="electronics"
        )
        # Create 10 fake products
        for _ in range(10):
            name = fake.company() + " " + fake.word().capitalize()
            slug = name.replace(" ", "-").lower()
            Product.objects.create(
                category=category,
                name=name,
                slug=slug,
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(100, 2000), 2),
                stock=random.randint(10, 100),
                available=True,
                image="products/placeholder.jpg"
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded the database with fake products."))
