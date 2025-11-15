StorePilot – Sales & Inventory Management System (Django + MySQL + Docker)

A powerful, modern, full-stack Sales & Inventory Management System built with Django, Bootstrap 5, AJAX, and MySQL.
Designed for small and medium businesses to manage products, sales, purchases, invoices, staff, and customers through a clean and intuitive UI.

<div align="center"> <img src="https://res.cloudinary.com/murste/image/upload/v1698907632/stevolve_x8ioeu.png" width="120" /> </div>
📌 Table of Contents

📌 Description

✨ Features

🖼️ Screenshots

🛠️ Tech Stack

📦 Project Structure

🚀 Installation Guide

🔧 1. Clone Repository

🐳 2. Run With Docker

💻 3. Run Without Docker

🐬 MySQL Configuration

📤 Deployment

👨‍💻 Author

📄 License

📌 Description

StorePilot is a complete business management system featuring:

✔ Inventory Management
✔ Dynamic Sales Processing (using AJAX)
✔ Vendor & Purchase Management
✔ Customer & Staff Management
✔ Billing and Invoice System
✔ Real-time stock updates
✔ Excel Export
✔ Docker + MySQL Support

Perfect for retail, wholesale, warehouse, and SMB operations.

✨ Features
🛒 Sales Management

AJAX-based item addition

Auto tax, subtotal, grand total & change calculation

Stock auto-deduct on sale

Sale detail view

Export sales to Excel

📦 Inventory Management

Add/Update/Delete products

Auto stock adjustments

Category-wise listing

🚚 Purchases & Vendors

Record purchases

Auto-increase stock

Vendor list

Purchase detail page

👥 Users

Customer list

Staff management

Django authentication system

🧾 Invoices & Bills

Generate invoices

Printable invoice layout

View bills

🎨 UI & UX

Bootstrap 5

Modern gradient theme

Smooth animations

Responsive tables

🧰 Misc

OpenPyXL export

Docker & Docker Compose support

MySQL ready

AJAX endpoints

🖼️ Screenshots

Place your screenshots inside /Assets/ folder.

<details> <summary>Click to view screenshots</summary>

</details>
🛠️ Tech Stack
Component	Technology
Backend	Django 5, Python 3.11+
Frontend	Bootstrap 5, HTML, JavaScript, AJAX
Database	MySQL (Prod), SQLite (Dev)
Containerization	Docker, Docker Compose
Exporting	OpenPyXL
Auth	Django Authentication
📦 Project Structure
StorePilot/
│── accounts/
│── bills/
│── invoice/
│── static/
│── store/
│── transactions/
│── StorePilot/              # Django settings
│── Assets/                  # Screenshots & media files
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
│── manage.py

🚀 Installation Guide
🔧 1. Clone Repository
git clone https://github.com/v4viki/StorePilot.git
cd StorePilot

🐳 2. Run With Docker (Recommended)

Start MySQL + Django:

docker-compose up --build -d


Apply migrations:

docker exec -it storepilot-web python manage.py migrate


Create admin:

docker exec -it storepilot-web python manage.py createsuperuser


Your app runs at:
👉 http://127.0.0.1:8000

💻 3. Run Without Docker
Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🐬 MySQL Configuration

Create a .env file:

DB_NAME=storepilot
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=db
DB_PORT=3306


Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

📤 Deployment (Production)

Supported Providers:

Render

Railway

AWS / EC2

DigitalOcean

Docker VPS

Build Production Image:

docker build -t storepilot:prod .


Run With Gunicorn:

gunicorn StorePilot.wsgi:application --bind 0.0.0.0:8000

📄 License

This project is licensed under the MIT License — free to use, share, and modify.

🎉 Thank You for Using StorePilot!

For improvements, issues, or suggestions — feel free to open a PR or issue.
