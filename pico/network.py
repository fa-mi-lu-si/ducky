import network
from time import time

SSID = "iPhone X"
PASSWORD = "MakerCulture7!"
# SSID = "Something"
# PASSWORD = "MakerCulture7!"

CONNECTION_TIMEOUT = 20  # Abort the connection after this many seconds

def connect_wifi(ssid, password):
    start_time = time()
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        station.active(True)
        station.connect(ssid, password)
        while (not station.isconnected()) and (
            time() - start_time < CONNECTION_TIMEOUT
        ):
            pass
    print(station.ifconfig())
    return station.isconnected()


print("Connecting to " + SSID + "...")
wifi_connected = connect_wifi(SSID, PASSWORD)
print(f"Connected : {wifi_connected}")
