import pygame.camera
import pygame.image

def takePhoto():
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, "trash.jpg")
    pygame.camera.quit()