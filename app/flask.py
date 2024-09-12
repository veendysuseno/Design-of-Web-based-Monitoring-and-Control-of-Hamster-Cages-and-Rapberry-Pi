from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL
import RPi.GPIO as GPIO

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'suhupi'

db = MySQL(app)

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)  # Fan pin GPIO 27
GPIO.setup(22, GPIO.OUT)  # Lamp pin GPIO 22

mode = 0
lampu = ""
kipas = ""

def fetch_latest_data():
    """Fetch the latest monitoring data from the database."""
    try:
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM monitoring ORDER BY id DESC LIMIT 1")
        rv = cur.fetchall()
        cur.close()

        if rv:
            row = rv[0]
            temp = row[1]
            hum = row[2]
            status = str(row[3])
            return temp, hum, status
        else:
            return None, None, "Data tidak tersedia"
    except Exception as e:
        return None, None, f"Error: {e}"

@app.route('/')
def index():
    global mode, kipas, lampu
    temp, hum, status = fetch_latest_data()
    
    if status == "Normal":
        kipas = "Tidak Aktif"
        lampu = "Tidak Aktif"
    elif status == "Kipas Hidup":
        kipas = "Aktif"
        lampu = "Tidak Aktif"
    elif status == "Lampu Hidup":
        kipas = "Tidak Aktif"
        lampu = "Aktif"
    
    return render_template('index.html', temp=temp, hum=hum, status=status, kipas=kipas, lampu=lampu)

@app.route('/otomatis')
def mode_otomatis():
    global mode
    mode = 1
    return index()

@app.route('/manual')
def mode_manual():
    global mode
    mode = 0
    return index()

@app.route('/kipas_mati')
def kipas_mati():
    global kipas
    kipas = "Tidak Aktif"
    if mode == 0:
        GPIO.output(27, GPIO.HIGH)  # Kipas Mati
    return index()

@app.route('/kipas_hidup')
def kipas_hidup():
    global kipas
    kipas = "Aktif"
    if mode == 0:
        GPIO.output(27, GPIO.LOW)  # Kipas Hidup
    return index()

@app.route('/lampu_mati')
def lampu_mati():
    global lampu
    lampu = "Tidak Aktif"
    if mode == 0:
        GPIO.output(22, GPIO.HIGH)  # Lampu Mati
    return index()

@app.route('/lampu_hidup')
def lampu_hidup():
    global lampu
    lampu = "Aktif"
    if mode == 0:
        GPIO.output(22, GPIO.LOW)  # Lampu Hidup
    return index()

@app.route('/data')
def ambildata():
    temp, hum, status = fetch_latest_data()
    return jsonify(temp=temp, hum=hum, status=status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
