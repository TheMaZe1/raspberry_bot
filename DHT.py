import time
import Adafruit_DHT

# Sensor data pin is connected to GPIO 4
sensor_name = Adafruit_DHT.DHT11
sensor_pin = 4


def get_value():
    hum, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
    return hum, temperature
