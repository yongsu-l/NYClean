import time
from sms import sendSMS
from camera import takePhoto
from watson import *
from auth import *

def main():
    try:
        """
        while True:
            sendSMS("This is Brooklyn", "+16463715825")
            time.sleep(2)
            """
        post_imageV2("Trash_1268903726", "trash.jpg", ibm_auth)
    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()