<div align="center">
  <h1>🚗 Smart Parking</h1>
  <p><strong>Intelligent Parking Management System</strong></p>
  <p>
    A modern web application designed to simplify and streamline the parking experience with real-time availability, secure reservations, and a user-friendly interface.
  </p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
  [![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange)](https://www.mysql.com/)
</div>

---

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## ℹ️ About
**Smart Parking** is a web application that addresses urban parking challenges by offering real-time parking availability, secure reservations, and an intuitive interface. Whether you're a driver seeking a hassle-free parking spot or a manager optimizing space allocation, Smart Parking delivers a seamless solution.

---

## ✨ Features
- **Responsive Welcome Page**: Stunning landing page with animated backgrounds, bold typography, and clear CTAs for sign-in/signup.
- **User Authentication**: Secure sign-up/sign-in with password hashing and session management.
- **Interactive Dashboard**: Realistic parking lot layout showing spaces (🟢 free, 🔴 occupied) with hover effects and real-time updates.
- **Reservation System**: Reserve a spot for 1–24 hours and receive a unique QR code for contactless entry.
- **User Profile**: View personal details (name, email, join date) in a clean, modern UI.
- **Reservation History**: Track past/active reservations with space number, times, and status (Active/Expired).
- **Mobile-First Design**: Fully responsive for phones, tablets, and desktops.
- **Animations & Micro-Interactions**: Subtle fade-ins, hover effects, and card transitions for a polished UX.

---

## 🛠️ Technologies
The project leverages a modern tech stack for reliability and scalability:

### Backend
- **Flask (2.3.3)**: Lightweight Python web framework for routing and server logic.
- **Flask-MySQLdb (1.0.1)**: MySQL integration for database operations.
- **Werkzeug (2.3.7)**: Secure password hashing and session management.
- **PyQRCode (7.4.2)** & **Pillow (10.0.0)**: QR code generation for reservations.

### Frontend
- **Bootstrap (5.3.2)**: Responsive grid system and UI components.
- **Font Awesome (6.4.2)**: Icons for intuitive navigation.
- **Animate.css (4.1.1)**: Smooth animations for dynamic effects.
- **Poppins Font**: Modern typography for a professional look.
- **Custom CSS**: Tailored styles for hero sections, buttons, and cards.

### Database
- **MySQL**: Relational database for users, parking spaces, and reservations.

### Other
- **Jinja2**: Templating engine for dynamic HTML rendering.
- **JavaScript**: Minimal scripts for client-side interactivity (e.g., form validation, animations).

---

## ⚙️ Installation
Follow these steps to set up **Smart Parking** locally:

### Prerequisites
- Python 3.8+
- MySQL Server (8.0+ recommended)
- pip (Python package manager)
- Git (for cloning the repository)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/smart-parking.git
   cd smart-parking

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
4. **Set Up MySQL Database**:
    Ensure MySQL is running.
    Log in to MySQL:
    ```bash
    mysql -u root -p 
    ```
    
   Create the database and tables
    ```bash
    CREATE DATABASE smart_parking;
    SOURCE init_db.sql;
    ```
    Update app.py and config.py with your MySQL credentials:
    ```bash
    app.config['MYSQL_USER'] = 'your_username'
    app.config['MYSQL_PASSWORD'] = 'your_password'
    ```
5. **Add Static Assets **:
    Place parking_layout.png and logo.png in static/images/.
    Ensure static/css/main.css and static/js/main.js are in place.
6. **Run the Application**:
     ```bash
    python app.py
    ```

## Technologies
Welcome Page: Vibrant hero section with "Sign In" or "Sign Up" options.
Sign Up: Create an account with name, email, and password.
Sign In: Log in to access the dashboard.
Dashboard: View parking spaces (🟢 free, 🔴 occupied). Click a free space to reserve.
Reservation: Select duration (1–24 hours), confirm, and receive a QR code.
Profile: Check account details (name, email, join date).
History: Review reservation history with space numbers, times, and statuses.
Logout: Sign out securely from the navigation bar.

## Project Structure
  ```bash
smart-parking/
├── static/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       ├── logo.png
│       └── parking_layout.png
├── templates/
│   ├── auth/
│   │   ├── signin.html
│   │   └── signup.html
│   ├── dashboard/
│   │   ├── home.html
│   │   └── reservation.html
│   ├── profile/
│   │   ├── profile.html
│   │   └── history.html
│   ├── base.html
│   └── index.html
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── parking.py
│   └── profile.py
├── app.py
├── config.py
├── models.py
├── init_db.sql
├── requirements.txt
└── README.md
    
  ```

app.py: Main Flask app with configuration and routes.
config.py: Database and secret key settings.
models.py: Database models for users, spaces, and reservations.
routes/: Modularized routes for auth, parking, and profile.
templates/: Jinja2 templates for HTML rendering.
static/: CSS, JS, and images for frontend.
init_db.sql: SQL script to initialize the database.


     
