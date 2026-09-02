import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

image_map = {
    "Gaming Mouse": "https://loremflickr.com/600/400/computer,mouse?lock=1",
    "USB-C Hub": "https://loremflickr.com/600/400/computer,usb?lock=1"
}

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
    except Exception as e:
        print(f"Error on {name}: {e}")
