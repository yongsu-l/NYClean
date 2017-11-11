import time
import os
from sms import sendSMS
from camera import takePhoto
from watson import post_imageV2
from auth import *

filename = "trash.jpg"

def main():
    try:
        """
        while True:
            sendSMS("This is Brooklyn", "+16463715825")
            time.sleep(2)
            """
        try:
            os.remove(filename)
            takePhoto()
            post_imageV2("Trash_523545137", filename, ibm_auth)
        except OSError:
            print("File delete failed")
    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()