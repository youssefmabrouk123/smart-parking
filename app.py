from flask import Flask, render_template, redirect, url_for
import os
from flask_mysqldb import MySQL

from config import Config  # Assure-toi que ce fichier s'appelle config.py


app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)


# Import and register blueprints
from routes.auth import auth_bp
from routes.parking import parking_bp
from routes.profile import profile_bp

app.register_blueprint(auth_bp)
app.register_blueprint(parking_bp)
app.register_blueprint(profile_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)