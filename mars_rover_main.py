from mars_rover import Rover
rover_number = 2

def main():
    gridx, gridy = map(int, input('GRID:').split()) #5 5
    all_coords = [] #For the final position of the first rover and the positions from which the following rovers move do not overlap.
    results = [] #For print the final positions of all the rovers at the end.
    check=True #For the check for wrong situations.

    for i in range(1,(rover_number+1)): 
        x, y, way = input('coordinates for rover %d:' %i).split() #1.rover: 1 2 N / 2.rover: 3 3 E
        rover = Rover(int(x), int(y), gridx, gridy, way)
        for j in input('instructions for rover %d:' %i): #1.rover: LMLMLMLMM / 2.rover: MMRMMRMRRM
            if j not in 'RLM': #For the check incorrect character input
                check=False
            else:
                if j=='R':
                    rover.turn_right()
                elif j=='L':
                    rover.turn_left()
                elif j=='M' :
                    rover.move()
                    if (rover.x, rover.y) in all_coords: #For the check if the moved location coincides with the previous rover location.
                        check=False
                    else:
                        continue
        if check==False:
            print('Something wrong rover can not move, try again.')
        else: #For the add to list and print the location of the rovers that have successfully completed the mission.
            all_coords.append((rover.x, rover.y))
            results.append((rover.x, rover.y, rover.way))

    for x, y, z in results:
            print(x, y, z) #1.rover: 1 3 N / 2.rover: 5 1 E

if __name__ == '__main__':
    main()