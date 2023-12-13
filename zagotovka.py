import os
import random
import sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('white'))


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

class Bob(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png", -1)
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bob.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom

# image = load_image("jorik.jpg")
# img_1 = pygame.transform.scale(image, (200, 100))
# img_2 = pygame.transform.scale(image, (100, 200))

all_sprites = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
# sprite.image = load_image('bob.png')
# sprite.rect = sprite.image.get_rect()
# all_sprites.add(sprite)
# sprite.rect.x = 5
# sprite.rect.y = 50

# bob_image = load_image('bob.png')
# for i in range(50):
#     bob = pygame.sprite.Sprite(all_sprites)
#     bob.image = bob_image
#     bob.rect = bob.image.get_rect()
#
#     bob.rect.x = random.randrange(width)
#     bob.rect.y = random.randrange(height)

for i in range(20):
    Bob(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.blit(image, (10, 10))
    # screen.blit(img_1, (150, 150))
    # screen.blit(img_2, (250, 250))
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update(event)
    pygame.display.flip()
pygame.quit()
