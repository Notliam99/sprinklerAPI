"""Manage the wifi on the board"""
from network import WLAN, STA_IF, AP_IF
from time import sleep


class wifi:
    """Connect to or setup a network."""

    def __init__(self, password: str, ssid: str):
        if password or ssid == "" or None:
            self.wlan = WLAN(AP_IF)
            self.wlan.config(
                essid="Sprikiley",
                hostname="sprikiley.local",
                security=0
            )
            self.wlan.active(True)
        else:
            self.password = password
            self.ssid = ssid
            self.wlan = WLAN(STA_IF)
            self.wlan.config(hostname="sprikiley.local")
            self.wlan.active(True)
            while self.wlan.isconnected() is False:
                print('Waiting for connection...')
                sleep(1)

        print(f"connected ({self.wlan.ifconfig()})")