import time
import os
from sms import sendSMS
from camera import takePhoto
from camera import initCamera
from watson import post_imageV2
from auth import ibm_auth

filename = "trash.jpg"

def main():
    try:
        cam = initCamera()
        while True:
            """
            sendSMS("This is Brooklyn", "+16463715825")
            time.sleep(2)
            """
            takePhoto(cam, filename)
            time.sleep(.5)
            if post_imageV2("TrashIdentifier_1448310972", filename, ibm_auth):
                print("Empty the fking trash")
            else:
                print("Don't empty trash")
    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()