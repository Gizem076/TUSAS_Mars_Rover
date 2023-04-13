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

if __name__ == '__main__':
    gridx, gridy = map(int, input('GRID:').split()) #5 5
    intersection = []
    all_coords = []
    results = []

    for i in range(1,(rover_number+1)):
        x, y, way = input('coordinates for rover %d:' %i).split() #1.rover: 1 2 N / 2.rover: 3 3 E
        if [x, y, way] not in all_coords:
            all_coords.append([x, y, way])
            rover = Rover(int(x), int(y), gridx, gridy, way, intersection)
            for j in input('instructions for rover %d:' %i): #1.rover: LMLMLMLMM / 2.rover: MMRMMRMRRM
                if j not in 'RLM':
                    print('Invalid instruction, use M or R or L and please try again')
                    exit()
                else:
                    if j=='R':
                        rover.turn_right()
                    elif j=='L':
                        rover.turn_left()
                    elif j=='M':
                        rover.move(intersection)
            intersection.append((rover.x, rover.y))
            results.append((rover.x, rover.y, rover.way))
        else:
            print('The both rover is in the same location,please enter another coordinate !')
            exit()