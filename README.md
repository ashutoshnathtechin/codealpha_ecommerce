# Amazone E-Commerce Platform

A fully functional, responsive e-commerce web application inspired by Amazon. Built with Django, this project features a dynamic shopping cart, a sleek modern UI, and a serverless deployment architecture.

## 🚀 Overview
**Amazone** is a full-stack e-commerce store designed to simulate a real-world shopping experience. It allows users to browse a catalog of realistic products, view dynamic hero-banner promotions, add items to their shopping cart without page reloads, and proceed through a simulated checkout flow.

## ✨ Key Features
- **Amazon-Inspired UI**: Custom CSS and Bootstrap 5 were used to replicate the iconic dark navbar, yellow pill-shaped "Add to Cart" buttons, and a dynamic fading hero carousel.
- **Asynchronous Shopping Cart**: Uses JavaScript `fetch` API to seamlessly add/remove items and update cart totals in real-time without reloading the page.
- **Relational Database**: Features a robust SQL schema managing `Customers`, `Products`, `Orders`, `OrderItems`, and `ShippingAddresses`.
- **Automated Data Seeding**: Includes custom Python scripts that auto-populate the database with realistic product names, prices, and high-quality images fetched directly from Unsplash.
- **Serverless Ready**: Configured with WhiteNoise and custom WSGI routing to deploy seamlessly on Vercel's serverless architecture.

## 🛠️ Tech Stack
- **Backend**: Python, Django 3.2
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite3
- **Static File Serving**: WhiteNoise
- **Deployment**: Vercel

## ⚙️ How It Works (Architecture)
1. **The Views**: Django renders the HTML templates (`store.html`, `cart.html`, etc.) and injects the database objects (like the product list and prices).
2. **The Logic**: When a user clicks "Add to Cart", a JavaScript function sends a hidden POST request to the `/update_item/` endpoint.
3. **The Models**: The Django backend receives this request and creates an `OrderItem` linked to the user's open `Order` (their cart). 
4. **Vercel Workaround**: Because Vercel uses a read-only filesystem, a custom script in `settings.py` copies the local SQLite database to the `/tmp/` directory on boot so the application can read the product data without crashing.

## 💻 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/ashutoshnathtechin/codealpha_ecommerce.git
cd codealpha_ecommerce
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the development server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to view the store!
