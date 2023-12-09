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

bob_image = load_image('bob.png')
for i in range(50):
    bob = pygame.sprite.Sprite(all_sprites)
    bob.image = bob_image
    bob.rect = bob.image.get_rect()

    bob.rect.x = random.randrange(width)
    bob.rect.y = random.randrange(height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.blit(image, (10, 10))
    # screen.blit(img_1, (150, 150))
    # screen.blit(img_2, (250, 250))
    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()
