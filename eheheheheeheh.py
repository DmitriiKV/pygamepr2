import os
import sys

import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((250, 250, 250))


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

class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height

class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, *args, **kwargs):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)

all_sprites = pygame.sprite.Group()

mountain = Mountain()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)
    screen.fill((250, 250, 250))
    all_sprites.draw(screen)
    all_sprites.update(event)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
