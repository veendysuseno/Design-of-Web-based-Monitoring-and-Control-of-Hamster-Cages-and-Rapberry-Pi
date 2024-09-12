from flask import Flask
from flask_mysqldb import MySQL
import RPi.GPIO as GPIO

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'suhupi'

# Inisialisasi MySQL
mysql = MySQL(app)

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)  # Fan pin GPIO 27
GPIO.setup(22, GPIO.OUT)  # Lamp pin GPIO 22

# Mode awal
mode = 0
lampu = ""
kipas = ""

# Import routing dari file lain
from . import routes
