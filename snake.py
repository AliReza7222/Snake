import consts


class Snake:

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)
        self.dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
        self.dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        x, y = self.dx[self.direction], self.dy[self.direction]
        x_p, y_p = self.cells[0]
        pos_new = x_p+x, y_p+y
        if pos_new == (19, 19):
            pos_new = (19, 0)
        elif pos_new == (0, 0):
            pos_new = (0, 19)
        elif pos_new == (0, 19):
            pos_new = (0, 0)
        elif pos_new == (19, 0):
            pos_new = (19, 19)
        self.cells.append(pos_new)

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