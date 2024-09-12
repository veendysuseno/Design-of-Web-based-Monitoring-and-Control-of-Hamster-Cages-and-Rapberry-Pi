import Adafruit_DHT
import RPi.GPIO as GPIO
import MySQLdb as mdb
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)  # Fan pin GPIO 27
GPIO.setup(22, GPIO.OUT)  # Lampu pin GPIO 22

# Setup sensor and database connection
sensor = Adafruit_DHT.DHT11
pin = 4
kondisi = "Normal"

try:
    con = mdb.connect('localhost', 'root', 'root', 'suhupi')
    cur = con.cursor()

    while True:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        waktu = time.strftime("%H:%M:%S")

        if hum is not None and temp is not None:
            print("Temp={0:0.1f}°C Humidity={1:0.1f}%".format(temp, hum))

            if temp > 30:
                GPIO.output(27, GPIO.LOW)  # Kipas Mati
                GPIO.output(22, GPIO.HIGH)  # Lampu Hidup
                kondisi = "Lampu Hidup"
            elif temp < 29:
                GPIO.output(27, GPIO.LOW)  # Kipas Mati
                GPIO.output(22, GPIO.HIGH)  # Lampu Hidup
                kondisi = "Lampu Hidup"
            else:
                GPIO.output(27, GPIO.LOW)  # Kipas Mati
                GPIO.output(22, GPIO.LOW)  # Lampu Mati
                kondisi = "Normal"

            try:
                sql = """INSERT INTO monitoring(suhu, kelembapan, kondisi) VALUES (%s, %s, %s)"""
                cur.execute(sql, (temp, hum, kondisi))
                con.commit()
            except mdb.Error as e:
                print(f"Error {e.args[0]}: {e.args[1]}")
                con.rollback()
        else:
            print('Failed to get reading. Try again!')

        time.sleep(10)  # Tunggu 10 detik sebelum pembacaan berikutnya

except mdb.Error as e:
    print(f"Database connection error: {e}")

finally:
    if con:
        con.close()
    GPIO.cleanup()  # Cleanup GPIO on exit
