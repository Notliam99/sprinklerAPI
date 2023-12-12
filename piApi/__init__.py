"""module with many utils and boilerplate code for the api"""

from .wifi import Wifi
from .utils.config import Config
from time import sleep

__version__ = 0.0


default_config = dict({
    "wifi": {
        "ssid": "",
        "password": ""
    }
})


class Api():
    def __init__(
        self,
        diy=False,
        default_config=default_config,
        config_name="config.json"
    ):
        if diy is True:
            pass

        self.config = Config(config_name, default_config)
        data = self.config.data

        wifi = Wifi(wifi_config=data["wifi"])

        sleep(200)
