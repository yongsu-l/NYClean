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
            for i in range(5):
                takePhoto(cam, filename)
                data = (post_imageV2("TrashIdentifier_1455385164", filename, ibm_auth))
                print(data['images'][0]['classifiers'][0]['classes'][0]['score'])
                score += (data['images'][0]['classifiers'][0]['classes'][0]['score'])
            
            score /= 5
            print(score)

            if score > 0.20:
                print("Is trash")
                sendSMS("This is Brooklyn", "+16463715825")
                time.sleep(2)

            else:
                print("Not trash")

    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()