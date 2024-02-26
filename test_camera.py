from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2560, 1936)
camera.capture('test.jpg')
