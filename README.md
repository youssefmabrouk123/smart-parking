Smart Parking - Intelligent Parking Management System

Smart Parking is a modern web application designed to simplify and streamline the parking experience. By leveraging real-time availability, secure reservations, and a user-friendly interface, it addresses common parking challenges in urban environments. Whether you're a driver looking for a hassle-free spot or a parking lot manager seeking efficient space allocation, Smart Parking delivers a seamless solution.
Table of Contents

Features
Technologies
Installation
Usage
Project Structure
Database Setup
Contributing
License
Contact

Features
Smart Parking offers a robust set of features to enhance the parking experience:

Responsive Welcome Page: A visually stunning landing page with animated backgrounds, bold typography, and clear calls-to-action for signing in or signing up.
User Authentication: Secure sign-up and sign-in functionality with password hashing and session management to protect user data.
Interactive Dashboard: A realistic parking lot layout displaying spaces (green for free, red for occupied) with hover effects and real-time status updates.
Reservation System: Reserve a parking space for a specified duration (1–24 hours) and receive a unique QR code for contactless entry.
User Profile: View personal details (name, email, join date) in a clean, modern interface.
Reservation History: Track past and active reservations with details like space number, start/end times, and status (Active/Expired).
Mobile-First Design: Fully responsive across devices, ensuring a smooth experience on phones, tablets, and desktops.
Animations & Micro-Interactions: Subtle fade-ins, hover effects, and card transitions for a polished, engaging user experience.

Technologies
The project is built with a modern tech stack for reliability and scalability:

Backend:
Flask (2.3.3): Lightweight Python web framework for routing and server logic.
Flask-MySQLdb (1.0.1): MySQL integration for database operations.
Werkzeug (2.3.7): Secure password hashing and session management.
PyQRCode (7.4.2) & Pillow (10.0.0): QR code generation for reservations.


Frontend:
Bootstrap (5.3.2): Responsive grid system and UI components.
Font Awesome (6.4.2): Icons for intuitive navigation and feature highlights.
Animate.css (4.1.1): Smooth animations for dynamic effects.
Poppins Font: Modern typography for a professional look.
Custom CSS: Tailored styles for hero sections, buttons, and cards.


Database:
MySQL: Relational database for storing users, parking spaces, and reservations.


Other:
Jinja2: Templating engine for dynamic HTML rendering.
JavaScript: Minimal scripts for client-side interactivity (e.g., form validation, animations).



Installation
Follow these steps to set up Smart Parking locally:
Prerequisites

Python 3.8+
MySQL Server (8.0+ recommended)
pip (Python package manager)
Git (for cloning the repository)

Steps

Clone the Repository:
git clone https://github.com/your-username/smart-parking.git
cd smart-parking


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Set Up MySQL Database:

Ensure MySQL is running.
Log in to MySQL:mysql -u root -p


Create the database and tables:CREATE DATABASE smart_parking;
SOURCE init_db.sql;


Update app.py and config.py with your MySQL credentials if different:app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'




Add Static Assets:

Place parking_layout.png and logo.png in static/images/. (Tip: Use a high-quality parking lot image, e.g., 800x400px.)
Ensure static/css/main.css and static/js/main.js are in place (provided in the repository).


Run the Application:
python app.py


Open http://localhost:5000 in your browser.



Usage

Welcome Page: Land on the homepage with a vibrant hero section. Click "Sign In" or "Sign Up" to proceed.
Sign Up: Create an account with your name, email, and password.
Sign In: Log in with your credentials to access the dashboard.
Dashboard: View available parking spaces (green) and occupied ones (red). Click a free space to reserve it.
Reservation: Select a duration (1–24 hours), confirm, and receive a QR code for entry.
Profile: Check your account details (name, email, join date).
History: Review your reservation history, including space numbers, times, and statuses.
Logout: Sign out securely from the navigation bar.

Project Structure
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


app.py: Main Flask application with configuration and route registration.
config.py: Database and secret key settings.
models.py: Database models for users, parking spaces, and reservations.
routes/: Modularized routes for authentication, parking, and profile features.
templates/: Jinja2 templates for rendering HTML pages.
static/: CSS, JavaScript, and images for frontend styling.
init_db.sql: SQL script to initialize the MySQL database.

Database Setup
The application uses a MySQL database with three tables:

users: Stores user details (id, name, email, password, created_at).
parking_spaces: Defines parking spaces (id, space_number, location).
reservations: Tracks reservations (id, user_id, space_id, start_time, end_time, created_at).

To set up:

Run init_db.sql to create the schema and seed 15 parking spaces (A1–A5, B1–B5, C1–C5).
Verify tables:USE smart_parking;
SHOW TABLES;
SELECT * FROM parking_spaces;



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch:git checkout -b feature/your-feature


Commit changes:git commit -m "Add your feature"


Push to your fork:git push origin feature/your-feature


Open a Pull Request with a clear description of your changes.

Please follow the code style, write tests if applicable, and ensure your changes don’t break existing functionality.
License
This project is licensed under the MIT License. See LICENSE for details.
Contact
For questions or feedback:

GitHub: your-username
Email: your.email@example.com

Thank you for exploring Smart Parking! 🚗✨
