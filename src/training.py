import pygame.camera
import pygame.image
import time
import os
import zipfile
from camera import initCamera
from camera import takePhoto
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from auth import ibm_auth


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def trainWatson():

    names = ["empty", "full"]

    cam = initCamera()

    for i in range(2):

        if not os.path.exists(names[i]):
            os.makedirs(names[i])

        for j in range(50):
            takePhoto(cam, names[i] + '/' + names[i] + str(j) + ".jpg")


        zipf = zipfile.ZipFile(names[i] + ".zip", 'w', zipfile.ZIP_DEFLATED)
        zipdir(names[i], zipf)
        zipf.close()

        if i == 0:
            confirmation = input("Read to proceed with full?: ")

            while confirmation != "yes":
                confirmation = input("Read to proceed with full?: ")


    visual_recognition = VisualRecognitionV3('2016-05-20', api_key=ibm_auth)

    with open(join(dirname(__file__), 'full.zip'), 'rb') as full, \
      open(join(dirname(__file__), 'empty.zip'), 'rb') as empty:
      
      print(json.dumps(visual_recognition.create_classifier('TrashIdentifier', _positive_examples=full, negative_examples=empty), indent=2))

trainWatson()