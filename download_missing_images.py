import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

image_map = {
    "Gaming Mouse": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39d7?q=80&w=600",
    "USB-C Hub": "https://images.unsplash.com/photo-1592840062770-bc370ce5f4b5?q=80&w=600",
    "Blender": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?q=80&w=600",
    "1984": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=600"
}

# Provide custom headers to avoid 404 or 403
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for name, url in image_map.items():
    try:
        product = Product.objects.get(name=name)
        if not product.image:
            print(f"Downloading image for {name}...")
            
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req) as response:
                img_data = response.read()
                
            from django.core.files.base import ContentFile
            product.image.save(
                os.path.basename(f"{name.replace(' ', '_').lower()}.jpg"),
                ContentFile(img_data)
            )
            product.save()
            print(f"Saved image for {name}")
    except Product.DoesNotExist:
        print(f"Product {name} not found")
    except Exception as e:
        print(f"Error on {name}: {e}")

print("Remaining images updated.")
