direction=['E','N','W','S'] #saatin tersi yönü
location_move={'E':(1,0),'W':(-1, 0),'N':(0, 1),'S':(0, -1)}
rover_number = 2

def turn_right(way,direction):
    new_way=direction[direction.index(way)-1]
    return new_way

def turn_left(way,direction):
    new_way=direction[(direction.index(way)+1)%len(direction)]
    return new_way

def move(way,gridx,gridy,x,y,location_move):
    new_location_x=int(x) + int(location_move[way][0])
    new_location_y=int(y) + int(location_move[way][1])
    if new_location_x>gridx or new_location_y>gridy:
        print('You cannot move forwad, grid is done')
    else:
        return [new_location_x,new_location_y,way]

gridx,gridy= map(int, input('GRID:').split())

all_coordinates=[] 
final_result=[] 

for i in range(1,(rover_number+1)):
    x, y, coordinates = input('coordinates for rover %d:' %i).split()
    x,y=int(x),int(y)
    move_coordinates=[] 
    move_coordinates.append([x,y,coordinates])
    if [x,y,coordinates] not in all_coordinates:
        all_coordinates.append([x,y,coordinates])
        for j in input('instructions for rover %d:' %i):
                if j not in 'RLM':
                    print('Invalid instruction, use M or R or L and please try again')
                    exit()
                else:
                    if j=='R':
                        move_coordinates.append([move_coordinates[0][0],move_coordinates[0][1],turn_right(move_coordinates[0][2],direction)])
                    elif j=='L':
                        move_coordinates.append([move_coordinates[0][0],move_coordinates[0][1],turn_left(move_coordinates[0][2],direction)])
                    else:
                        move_coordinates.append(move(move_coordinates[0][2],gridx,gridy,move_coordinates[0][0],move_coordinates[0][1],location_move))
                    move_coordinates.pop(0)
    else:
        print('The both rover is in the same location,please enter another coordinate !')