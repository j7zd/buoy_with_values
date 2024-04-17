import network
import time
import urequests
import ujson
from machine import UART, Pin

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=0, parity=None, stop=1)

print("Connecting to WiFi", end="")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Buoy", "shrekisloveshrekislife")
while not wlan.isconnected():
  print(".", end="")
  time.sleep(0.5)
print(" Connected!")
print(wlan.ifconfig())

i = 0

while True:
    json = uart.read()
    if json is None:
        continue
    print(str(i) + ': ' + str(json))
    i += 1
    r = urequests.post("http://192.168.157.236:5000", headers = {'content-type': 'application/json'}, data=json[:-2])

