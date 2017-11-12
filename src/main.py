""" NYClean """

import time
from sms import sendSMS
from camera import takePhoto
from camera import initCamera
from watson import post_imageV2
from auth import ibm_auth

def main():
    trash_filename = "trash.jpg"
    try:
        cam = initCamera()
        while True:
            """
            """
            score = 0
            for i in range(5):
                takePhoto(cam, trash_filename)
                data = (post_imageV2("TrashIdentifier_968106762", trash_filename, ibm_auth))
                print(data['images'][0]['classifiers'][0]['classes'][0]['score'])
                score += (data['images'][0]['classifiers'][0]['classes'][0]['score'])
            
            score /= 5
            print(score)

            if score > 0.20:
                print("Is trash")
                sendSMS("Garbage can is full!!!!", "+16465411524")
                time.sleep(2)

            else:
                print("Not trash")

    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()