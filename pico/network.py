import network
from config_tool import read_json_file
from time import time

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


config = read_json_file("config.jsonc")
if config:
    SSID = config["SSID"]
    PASSWORD = config["PASSWORD"]

    print("Connecting to " + SSID + "...")
    wifi_connected = connect_wifi(SSID, PASSWORD)
    print(f"Connected : {wifi_connected}")
