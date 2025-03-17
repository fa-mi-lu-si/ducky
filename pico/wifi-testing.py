import network
from machine import Pin

ssid = "testnetwork"
password = "nath2068"

led = Pin("LED",Pin.IN)

def connect_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        pass
    print("Connection successful")
    print(station.ifconfig())

led.off()
connect_wifi(ssid,password)
led.on()
