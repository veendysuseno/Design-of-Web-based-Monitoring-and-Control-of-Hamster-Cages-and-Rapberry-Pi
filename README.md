# Design of Web-based Monitoring and Control of Hamster Cages and Raspberry Pi

![images-hamster](static/images/hamster.png)<br/>

## Overview

This project is a web-based system designed to monitor and control hamster cages using a Raspberry Pi. The system features real-time data monitoring and control of the hamster cage environment, including temperature and humidity. Users can interact with the system via a web interface to manage fan and light settings.

## Features

- **Real-time Monitoring:** Displays the latest temperature, humidity, and status of the hamster cage.
- **Control Interface:** Allows users to manually or automatically control the fan and light based on temperature readings.
- **Web Interface:** Accessible via a browser, offering buttons to switch between manual and automatic modes and control the fan and light.

## Project Structure

- `app/`

  - `__init__.py`: Initializes the Flask application and configures MySQL and GPIO.
  - `routes.py`: Defines the routes and logic for rendering the HTML templates and interacting with the MySQL database.
  - `raspi.py`: Handles sensor readings and updates the database with temperature and humidity data.
  - `flask.py`: The main Flask application file containing route definitions and GPIO control logic.

- `static/`

  - `css/`
    - `styles.css`: Contains the styles for the web interface.
  - `js/`
    - `scripts.js`: Contains the JavaScript code for dynamic interactions on the web page.

- `templates/`
  - `index.html`: The main HTML template for the web interface.

## Setup

### Prerequisites

- Raspberry Pi with Raspbian OS
- Python 3.x
- Flask
- Flask-MySQLdb
- Adafruit-DHT library
- MySQL Server

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/Design-of-Web-based-Monitoring-and-Control-of-Hamster-Cages-and-Raspberry-Pi.git
cd Design-of-Web-based-Monitoring-and-Control-of-Hamster-Cages-and-Raspberry-Pi
```

2. Install Dependencies
   - Install the required Python packages:

```bash
pip install flask flask-mysqldb Adafruit-DHT
```

3. Setup the MySQL Database
   - Create the database and table for storing monitoring data:

```bash
CREATE DATABASE suhupi;
USE suhupi;
CREATE TABLE monitoring (
    id INT AUTO_INCREMENT PRIMARY KEY,
    suhu FLOAT,
    kelembapan FLOAT,
    kondisi VARCHAR(255)
);
```

4. Configure GPIO and Sensor
   - Connect the DHT11 sensor to the Raspberry Pi and set up GPIO pins as specified in raspi.py.
5. Run the Application
   - Start the Flask application:

```bash
python app/flask.py
```

- Access the web interface by navigating to http://<raspberry-pi-ip>:5000 in your web browser.

## sage

- Mode Manual: Switch to manual control mode where you can directly control the fan and light.
- Mode Otomatis: Switch to automatic mode where the fan and light are controlled based on temperature readings.
- Kipas Mati/Hidup: Turn the fan on or off.
- Lampu Mati/Hidup: Turn the light on or off.
- Data: Retrieve the latest temperature, humidity, and status data from the database.

## Notes

- Ensure that the Raspberry Pi has access to the MySQL server and the necessary Python libraries are installed.
- Adjust the GPIO pins in the raspi.py and flask.py files if you are using different pins.
