import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Category, Product

def populate_more():
    electronics, _ = Category.objects.get_or_create(name="Electronics")
    clothing, _ = Category.objects.get_or_create(name="Clothing")
    home, _ = Category.objects.get_or_create(name="Home & Kitchen")
    books, _ = Category.objects.get_or_create(name="Books")

    more_products = [
        {"name": "4K Ultra HD TV", "price": "499.99", "category": electronics, "desc": "Stunning 4K resolution television."},
        {"name": "Bluetooth Speaker", "price": "45.00", "category": electronics, "desc": "Portable waterproof bluetooth speaker."},
        {"name": "Gaming Mouse", "price": "29.99", "category": electronics, "desc": "RGB gaming mouse with adjustable DPI."},
        {"name": "Mechanical Keyboard", "price": "89.99", "category": electronics, "desc": "Clicky mechanical keyboard for typing and gaming."},
        {"name": "USB-C Hub", "price": "35.50", "category": electronics, "desc": "Multi-port USB-C adapter."},
        {"name": "Men's Winter Coat", "price": "120.00", "category": clothing, "desc": "Warm and stylish winter coat."},
        {"name": "Running Shoes", "price": "85.00", "category": clothing, "desc": "Lightweight running shoes."},
        {"name": "Graphic Hoodie", "price": "40.00", "category": clothing, "desc": "Comfortable hoodie with a cool graphic."},
        {"name": "Yoga Pants", "price": "25.00", "category": clothing, "desc": "Stretchable and breathable yoga pants."},
        {"name": "Sunglasses", "price": "15.99", "category": clothing, "desc": "UV protection sunglasses."},
        {"name": "Coffee Maker", "price": "55.00", "category": home, "desc": "Drip coffee maker with programmable timer."},
        {"name": "Blender", "price": "45.99", "category": home, "desc": "High-speed blender for smoothies."},
        {"name": "Non-Stick Pan Set", "price": "65.00", "category": home, "desc": "Durable non-stick frying pans."},
        {"name": "Vacuum Cleaner", "price": "150.00", "category": home, "desc": "Powerful bagless vacuum cleaner."},
        {"name": "Bed Sheets Set", "price": "35.00", "category": home, "desc": "Soft microfiber bed sheets."},
        {"name": "The Great Gatsby", "price": "10.99", "category": books, "desc": "Classic novel by F. Scott Fitzgerald."},
        {"name": "Atomic Habits", "price": "16.99", "category": books, "desc": "Bestselling self-help book by James Clear."},
        {"name": "1984", "price": "9.99", "category": books, "desc": "Dystopian novel by George Orwell."},
        {"name": "Sapiens", "price": "14.99", "category": books, "desc": "A brief history of humankind."},
        {"name": "Python Crash Course", "price": "22.50", "category": books, "desc": "A hands-on, project-based introduction to programming."}
    ]

    for i, p in enumerate(more_products):
        # We assign some generic realistic looking placeholder images using Unsplash keywords
        # or LoremFlickr
        obj, created = Product.objects.get_or_create(
            name=p["name"],
            defaults={
                "price": p["price"],
                "category": p["category"],
                "description": p["desc"]
            }
        )
        if created:
            print(f"Added new product: {p['name']}")

    print("Added 20 new products successfully!")

if __name__ == "__main__":
    populate_more()
