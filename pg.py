import os
import random
import sys

import pygame

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

player = None
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


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


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def start_screen(flag=True):
    intro_text = ["Заставка", "", "Правила игры", "Выход"]
    fon = pygame.transform.scale(load_image('BG.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_renderer = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_renderer.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_renderer, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(30)

tiles_image = {
    'wall': pygame.transform.scale(load_image('box.png'), (50, 50)),
    'empty': pygame.transform.scale(load_image('grass.png'), (50, 50))

}
player_image = pygame.transform.scale(load_image('mario.png'), (50, 50))
tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tiles_image[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)


class Camera:
    def __init__(self, field_size):
        self.x = 0
        self.y = 0
        self.fied_size = field_size

    def apply(self, obj):
        obj.rect.x += self.x
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.fied_size[0] + 1) * obj.rect.width
        if obj.rect.x >= (self.fied_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.fied_size[0])
        obj.rect.y += self.y
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.fied_size[1] + 1) * obj.rect.height
        if obj.rect.y >= (self.fied_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.fied_size[1])

    def update(self, target):
        self.x = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.y = -(target.rect.y + target.rect.h // 2 - height // 2)

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


clock = pygame.time.Clock()
start_screen()
player, level_x, level_y = generate_level(load_level('level.txt'))
camera = Camera((level_x, level_y))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 10
            if event.key == pygame.K_RIGHT:
                player.rect.x += 10
            if event.key == pygame.K_UP:
                player.rect.y -= 10
            if event.key == pygame.K_DOWN:
                player.rect.y += 10

    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(30)
terminate()