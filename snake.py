import consts


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
        pass

    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                if self.keys[key] == self.direction:
                    continue
                elif self.keys[key] == "UP" and self.direction == "DOWN":
                    continue
                elif self.keys[key] == "DOWN" and self.direction == "UP":
                    continue
                elif self.keys[key] == 'LEFT' and self.direction == 'RIGHT':
                    continue
                elif self.keys[key] == 'RIGHT' and self.direction == 'LEFT':
                    continue
                else:
                    self.direction = self.keys[key]