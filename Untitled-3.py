#!/usr/bin/python
import RPi.GPIO as GPIO
import dht11
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)