import os
import sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
image = pygame.Surface([100, 100])


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"файл с изображением вот таким -> {fullname} <- не найден!!!")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


image = load_image("jorik.jpg")
img_1 = pygame.transform.scale(image, (200, 100))
img_2 = pygame.transform.scale(image, (100, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, (10, 10))
    screen.blit(img_1, (150, 150))
    screen.blit(img_2, (250, 250))

    pygame.display.flip()
pygame.quit()
