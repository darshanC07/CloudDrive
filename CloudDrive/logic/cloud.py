"""
    This file contains the logic for the cloud cloud provider setup.
"""
from filestack import Client, Security
import time

class CloudSetup():
    """
        This class contains the logic for the cloud cloud provider setup.
    """

    def __init__(self, cloud_provider, api_key):
        """
            This is the constructor for the class.
            Checks the cloud provider and calls the respective method.
        """
        self.client = None
        self.cloud_provider = cloud_provider
        self.api_key = api_key
        
        if cloud_provider == "Filestack":
            self.filestack_setup(api_key)
        else:
            pass
    
    def filestack_setup(self, api_key, **kargs):
        # Initialize the client
        self.client = Client("api_key")
        print("Filestack setup done")

