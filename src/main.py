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
            """
            score = 0
            for _ in range(20):
                takePhoto(cam, filename)
                time.sleep(.5)
                data = post_imageV2("TrashIdentifier_1448310972", filename, ibm_auth)
                score += (data['images'][0]['classifiers'][0]['classes'][0]['score'])

            score /= 20

            if score > 0.30:
                sendSMS("This is Brooklyn", "+16463715825")
                time.sleep(2)

    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()