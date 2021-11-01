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
    # incomplate func
    def next_move(self):
        block = consts.block_cells
        x, y = self.dx[self.direction], self.dy[self.direction]
        x_p, y_p = self.get_head()
        x_new, y_new = x_p+x, y_p+y
        if x_new == 20:
            x_new = 0
        elif x_new == -1:
            x_new = 19
        elif y_new == 20:
            y_new = 0
        elif y_new == -1:
            y_new = 19

        pos_new = (x_new, y_new)
        pos_snakes = [s.cells for s in self.game.snakes]
        kill_cells = []

        for list_cell in pos_snakes:
            for tuple_cell in list_cell:
                kill_cells.append(tuple_cell)

        if (pos_new in self.cells) or (list(pos_new) in block) or (pos_new in kill_cells):
            self.game.kill(self)

        elif pos_new in self.game.list_frouit:
            self.game.list_frouit.remove(pos_new)
            self.cells.append(pos_new)
            self.game.get_cell(pos_new).set_color(self.color)

        elif pos_new not in self.game.list_frouit:
            whit_cell = self.cells[0]
            self.cells.append(pos_new)
            self.cells.remove(self.cells[0])
            self.game.get_cell(whit_cell).set_color(consts.back_color)
            self.game.get_cell(pos_new).set_color(self.color)

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