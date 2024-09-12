from flask import render_template, request, jsonify
from . import app, mysql
import RPi.GPIO as GPIO

@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM monitoring ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
        cur.close()

        if result:
            temp = result[1]
            hum = result[2]
            status = result[3]
        else:
            temp = hum = status = "Data tidak tersedia"

    except Exception as e:
        temp = hum = status = "Error: " + str(e)

    return render_template('index.html', temp=temp, hum=hum, status=status)

# Tambahkan route lain sesuai kebutuhan
