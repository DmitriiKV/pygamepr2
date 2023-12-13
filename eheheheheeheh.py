import os
import random
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


# class Bob(pygame.sprite.Sprite):
#     image = load_image("bomb.png")
#     image_boom = load_image("boom.png", -1)
#     def __init__(self, *group):
#         super().__init__(*group)
#         self.image = Bob.image
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(width)
#         self.rect.y = random.randrange(height)
#
#     def update(self, *args):
#         self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
#         if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
#             self.image = self.image_boom

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('red'), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randrange(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self, *args, **kwargs):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizon_bords):
            self.vy = - self.vy
        if pygame.sprite.spritecollideany(self, vertical_bords):
            self.vx = - self.vx

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_bords)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizon_bords)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

all_sprites = pygame.sprite.Group()

horizon_bords = pygame.sprite.Group()
vertical_bords = pygame.sprite.Group()

Border(5, 5, width-5, 5)
Border(5, height-5, width-5, height-5)
Border(5, 5, 5, height-5)
Border(width-5, 5, width-5, height-5)

for i in range(50):
    Ball(20, 100, 100)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.blit(image, (10, 10))
    # screen.blit(img_1, (150, 150))
    # screen.blit(img_2, (250, 250))
    screen.fill((250, 250, 250))
    all_sprites.draw(screen)
    all_sprites.update(event)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
