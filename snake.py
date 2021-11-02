import consts
import pygame

class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):

        nx = self.get_head()[0] + self.dx[self.direction]
        ny = self.get_head()[1] + self.dy[self.direction]

        nx = self.val(nx)
        ny = self.val(ny)

        cell = self.game.get_cell((nx, ny))
        cell_new = nx, ny

        if not cell or cell.color != consts.fruit_color and cell.color != consts.back_color:
            pygame.mixer.music.load("Game Over SFX and Voice.mp3")
            pygame.mixer.music.play()
            self.game.kill(self)
            return

        self.cells.append(cell_new)

        if cell.color != consts.fruit_color :
            whit_cell = self.cells.pop(0)
            self.game.get_cell(whit_cell).set_color(consts.back_color)

        if cell.color == consts.fruit_color:
            pygame.mixer.music.load("sound.ogg")
            pygame.mixer.music.play()
        cell.set_color(self.color)

    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                if self.keys[key] == self.direction:
                    continue
                if self.keys[key] == "UP" and self.direction == "DOWN":
                    continue
                if self.keys[key] == "DOWN" and self.direction == "UP":
                    continue
                if self.keys[key] == 'LEFT' and self.direction == 'RIGHT':
                    continue
                if self.keys[key] == 'RIGHT' and self.direction == 'LEFT':
                    continue
                else:
                    self.direction = self.keys[key]
            break