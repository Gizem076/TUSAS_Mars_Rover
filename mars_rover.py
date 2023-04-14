direction = ['N', 'E', 'S', 'W']
location_move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

class Rover:
    def __init__(self, x, y, gridx, gridy, way):
        self.x = x
        self.y = y
        self.gridx = gridx
        self.gridy = gridy
        self.way = way

    def turn_right(self):
        self.way = direction[(direction.index(self.way) + 1) % len(direction)]

    def turn_left(self):
        self.way = direction[(direction.index(self.way) - 1)]

    def move(self):
        new_loc_x = self.x + location_move[self.way][0]
        new_loc_y = self.y + location_move[self.way][1]
        if new_loc_x >= 0 and new_loc_y >= 0:
            self.x = new_loc_x
            self.y = new_loc_y
        else:
            exit()
        








