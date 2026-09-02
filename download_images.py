import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

image_map = {
    "Wireless Headphones": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600",
    "Smart Watch": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=600",
    "Laptop": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=600",
    "Cotton T-Shirt": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=600",
    "Jeans": "https://images.unsplash.com/photo-1542272604-787c3835535d?q=80&w=600",
    "Sneakers": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=600",
    "4K Ultra HD TV": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?q=80&w=600",
    "Bluetooth Speaker": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?q=80&w=600",
    "Gaming Mouse": "https://images.unsplash.com/photo-1599518532481-301a0cd22684?q=80&w=600",
    "Mechanical Keyboard": "https://images.unsplash.com/photo-1595225476474-87563907a212?q=80&w=600",
    "USB-C Hub": "https://images.unsplash.com/photo-1623838612165-27a3c306fa0d?q=80&w=600",
    "Men's Winter Coat": "https://images.unsplash.com/photo-1559551409-dadc959f76b8?q=80&w=600",
    "Running Shoes": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=600",
    "Graphic Hoodie": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?q=80&w=600",
    "Yoga Pants": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=600",
    "Sunglasses": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?q=80&w=600",
    "Coffee Maker": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?q=80&w=600",
    "Blender": "https://images.unsplash.com/photo-1585237704780-e840a1b6540c?q=80&w=600",
    "Non-Stick Pan Set": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?q=80&w=600",
    "Vacuum Cleaner": "https://images.unsplash.com/photo-1558317374-067fb5f30001?q=80&w=600",
    "Bed Sheets Set": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?q=80&w=600",
    "The Great Gatsby": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=600",
    "Atomic Habits": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=600",
    "1984": "https://images.unsplash.com/photo-1621360841013-c76831f185b3?q=80&w=600",
    "Sapiens": "https://images.unsplash.com/photo-1588666309990-d68f08e3d4a6?q=80&w=600",
    "Python Crash Course": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=600"
}

for name, url in image_map.items():
    try:
        product = Product.objects.get(name=name)
        if not product.image:
            print(f"Downloading image for {name}...")
            result = urllib.request.urlretrieve(url)
            product.image.save(
                os.path.basename(f"{name.replace(' ', '_').lower()}.jpg"),
                File(open(result[0], 'rb'))
            )
            product.save()
            print(f"Saved image for {name}")
    except Product.DoesNotExist:
        print(f"Product {name} not found")
    except Exception as e:
        print(f"Error on {name}: {e}")

print("All images updated.")
