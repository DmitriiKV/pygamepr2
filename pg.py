import os
import random
import sys

import pygame

FPS = 50
WIDTH = 400
HEIGHT = 400
GRAVITY = 0.25

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден!")
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


# class AnimateSprite(pygame.sprite.Sprite):
#     def __init__(self, sheet, columns, rows, x, y):
#         super().__init__(all_sprites)
#         self.frame = []
#         self.cut_sheet(sheet, columns, rows)
#         self.current_frame = 0
#         self.image = self.frame[self.current_frame]
#         self.rect = self.rect.move(x, y)
#
#     def cut_sheet(self, sheet, columns, rows):
#         self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
#         for i in range(rows):
#             for j in range(columns):
#                 frame_location = (self.rect.w * j, self.rect.h * i)
#                 self.frame.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
#
#     def update(self, *args, **kwargs):
#         self.current_frame = (self.current_frame + 1) % len(self.frame)
#         self.image = self.frame[self.current_frame]


# animate = AnimateSprite(load_image('knight.png'), 6, 1, 50, 50)

screen_rect = (0 , 0, WIDTH, HEIGHT)

class Particle(pygame.sprite.Sprite):
    fire = [pygame.transform.scale(load_image('jorik.jpg'), (20, 20))]
    for scale in range(5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))
    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self, *args, **kwargs):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()

def create_particles(position):
    particles_count = 50
    speed = range(-5, 6)
    for _ in range(particles_count):
        Particle(position, random.choice(speed), random.choice(speed))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_particles(pygame.mouse.get_pos())

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
terminate()
