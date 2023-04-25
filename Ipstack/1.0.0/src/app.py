import socket
import asyncio
import time
import random
import json
import requests

from walkoff_app_sdk.app_base import AppBase

class PythonPlayground(AppBase):
    __version__ = "1.0.0"
    app_name = "ipstack"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)


    # Write your data inside this function
    def get_location(self, access_key, ip):
        # It comes in as a string, so needs to be set to JSON
       url = f"http://api.ipstack.com/{ip}?access_key={access_key}"
       try:
            res= requests.get(url,verify=False)
       except Exception as e:
            return "Couldn't fetch the data: %s" % e
       
       return res.json()
    
    

if __name__ == "__main__":
    PythonPlayground.run()
