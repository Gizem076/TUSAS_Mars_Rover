from mars_rover import Rover
rover_number = 2

def main():
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

    for x, y, z in results:
        print(x, y, z) #1.rover: 1 3 N / 2.rover: 5 1 E