import pygame.camera
import pygame.image
import time
from cv2 import *

def initCamera():
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    return cam

def takePhoto(cam, filename):
    img = cam.get_image()
    pygame.image.save(img, filename)