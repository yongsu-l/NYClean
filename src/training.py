import pygame.camera
import pygame.image
import time
import os
import zipfile
from camera import *

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

        for i in range(50):
            takePhoto(cam, names[i], names[i] + '/' + names[i] + ".jpg")

        confirmation = input("Read to proceed with full?: ")

        while confirmation != "yes":
            confirmation = input("Read to proceed with full?: ")
        zipf = zipfile.ZipFile(names[i] + ".zip", 'w', zipfile.ZIP_DEFLATED)
        zipdir(names[i], zipf)
        zipf.close()

trainWatson()