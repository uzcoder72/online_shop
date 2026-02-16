# Django Online Shop

> [!TIP]
> **New to the project? Start here:**  
> 👉 [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)

## Project Overview

This is a **Django-based E-commerce** application designed to sell luxury goods and electronics. It features a fully functional shopping experience with product categorization, sorting, search functionality, and a custom user authentication system.

### Key Features
- **Custom User Model**: Handles customer profiles efficiently.
- **Product Management**: Filter by price ("Cheap" / "Expensive"), sort by categories, and search by name.
- **Dynamic UI**: Responsive Bootstrap design with a polished "About Us" page.
- **Admin Panel**: Customized Django admin for easy management of products, orders, and comments.

## Screenshots

### 1. Home Page & Shopping
*The main storefront displaying luxury items with "Sale" badges and price filtering.*
![Shop Home](screenshots/shop_home.png)

### 2. About Us
*A responsive team section highlighting our developers.*
![About Page](screenshots/shop_about.png)

### 3. Admin Dashboard
*Comprehensive backend management for store administrators.*
![Admin Panel](screenshots/shop_admin.png)

---

## Getting Started

1.  **Clone the repository.**
2.  **Follow the setup guide**: Read [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) for detailed steps on:
    -   Installing dependencies (Python 3.12+ recommended).
    -   Configuring the MySQL database in `.env`.
    -   Running migrations.
    -   Starting the server.

### Quick Start
```bash
# Install dependencies
python -m pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Enjoy shopping! 🛒
