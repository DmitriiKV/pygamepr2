import pygame
import random


class Board:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        for el in range(mines):
            self.board[random.randrange(0, height)][random.randrange(0, width)] = 10

        self.left = 5
        self.top = 5
        self.cell_size = 30
        self.mines = mines

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 10:
                    pygame.draw.rect(screen, pygame.Color('red'),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def get_click(self, mousepos):
        cell = self.get_cell(mousepos)
        if cell:
            self.on_click(cell)

    def get_cell(self, mousepos):
        cellx = ((mousepos[0] - self.left) // self.cell_size)
        celly = ((mousepos[1] - self.top) // self.cell_size)
        if cellx < 0 or cellx >= self.width or celly < 0 or celly >= self.height:
            return None
        return self.open_cell(cellx, celly)

    def open_cell(self, cc):
        global c
        c = 0
        for xx in range(cc[0] - 1, cc[0] + 1):
            for yy in range(y - 1, y + 1):
                if self.board[xx][yy] == 10:
                    c += 1

        return c

    def on_click(self, cellcoords):
        for i in range(self.width):
            self.board[cellcoords[1]][i] = (self.board[cellcoords[1]][i] + 1) % 2
        for i in range(self.height):
            if i == cellcoords[1]:
                continue
            self.board[i][cellcoords[0]] = (self.board[i][cellcoords[0]] + 1) % 2


def main():
    pygame.init()

    running = True

    board = Board(int(input()), int(input()), int(input()))
    print(board.board)
    size = width, height = board.width * board.cell_size + board.left * 2, board.height * board.cell_size + board.top * 2
    screen = pygame.display.set_mode(size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                font = pygame.font.Font(None, 2)
                text = font.render(f"{123}", True, (100, 255, 100))
                text_x = board.width // 2 - text.get_width() // 2
                text_y = board.height // 2 - text.get_height() // 2
                text_w = text.get_width()
                text_h = text.get_height()
                screen.blit(text, (text_x, text_y))
                board.get_click(event.pos)

        screen.fill(pygame.Color('black'))
        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
