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