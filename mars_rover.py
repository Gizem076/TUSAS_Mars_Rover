direction = ['N', 'E', 'S', 'W']
location_move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
rover_number = 2

class Rover:
    def __init__(self, x, y, gridx, gridy, way, intersection):
        self.x = x
        self.y = y
        self.gridx = gridx
        self.gridy = gridy
        self.way = way

    def turn_right(self):
        self.way = direction[(direction.index(self.way) + 1) % len(direction)]

    def turn_left(self):
        self.way = direction[(direction.index(self.way) - 1)]

    def move(self,intersection):
        new_loc_x = self.x + location_move[self.way][0]
        new_loc_y = self.y + location_move[self.way][1]
        if (new_loc_x, new_loc_y) not in intersection:
            if new_loc_x > self.gridx and new_loc_y > self.gridy:
                print('You can not move forwad, grid is done')
                exit()
            elif new_loc_x >= 0 and new_loc_y >= 0:
                self.x = new_loc_x
                self.y = new_loc_y
        else:
            print('The both rover is in the same location,please enter another coordinate')
            exit()