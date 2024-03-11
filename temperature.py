import time
import Adafruit_DHT

# Sensor data pin is connected to GPIO 4
sensor_name = Adafruit_DHT.DHT11
sensor_pin = 4

while True:
    hum, tenperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
    print(hum, tenperature)
    time.sleep(3.0)