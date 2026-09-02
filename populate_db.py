import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Category, Product
from django.contrib.auth.models import User

def populate():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin")
        print("Admin user created: admin / admin")

    if not User.objects.filter(username="testuser").exists():
        User.objects.create_user("testuser", "test@example.com", "password")
        print("Test user created: testuser / password")

    electronics, _ = Category.objects.get_or_create(name="Electronics")
    clothing, _ = Category.objects.get_or_create(name="Clothing")

    products_data = [
        {"name": "Wireless Headphones", "price": "99.99", "category": electronics, "desc": "High quality wireless headphones."},
        {"name": "Smart Watch", "price": "149.99", "category": electronics, "desc": "Feature-packed smartwatch."},
        {"name": "Laptop", "price": "999.99", "category": electronics, "desc": "Powerful laptop."},
        {"name": "Cotton T-Shirt", "price": "19.99", "category": clothing, "desc": "Comfortable 100% cotton t-shirt."},
        {"name": "Jeans", "price": "49.99", "category": clothing, "desc": "Classic denim jeans."},
        {"name": "Sneakers", "price": "79.99", "category": clothing, "desc": "Stylish and comfortable sneakers."}
    ]

    for p in products_data:
        obj, created = Product.objects.get_or_create(
            name=p["name"],
            defaults={
                "price": p["price"],
                "category": p["category"],
                "description": p["desc"]
            }
        )
        if created:
            print(f"Created product: {p['name']}")

    print("Database populated successfully!")

if __name__ == "__main__":
    populate()
