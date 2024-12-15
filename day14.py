import re
from functools import reduce
from statistics import variance

f      = open ( "2024\\day14.txt" , "r" )
guards = f.read().splitlines()
guards = [[ int(i) for i in re.findall ( r"-?\d+", guard ) ] for guard in guards]

quadrants = [0,0,0,0]
positions = []

WIDTH   = 101
HEIGHT  = 103

WIDTH_MIDDLE  = (WIDTH  // 2)
HEIGHT_MIDDLE = (HEIGHT // 2)

x_movement = []
y_movement = []

seconds = 100


for guard in guards:
    x, y, vx, vy = guard

    x_movement.append( (x, vx) )
    y_movement.append( (y, vy) )

    end_x = ( (x + seconds * vx) % WIDTH  )
    end_y = ( (y + seconds * vy) % HEIGHT )

    if   end_x < WIDTH_MIDDLE and end_y < HEIGHT_MIDDLE:
        quadrants[0] += 1
    elif end_x > WIDTH_MIDDLE and end_y < HEIGHT_MIDDLE:
        quadrants[1] += 1
    elif end_x < WIDTH_MIDDLE and end_y > HEIGHT_MIDDLE:
        quadrants[2] += 1
    elif end_x > WIDTH_MIDDLE and end_y > HEIGHT_MIDDLE:
        quadrants[3] += 1


safety_level = reduce ( lambda a, b: a * b, quadrants )

print(safety_level)

variances_x = []
variances_y = []

step_x     = 0
step_y     = 0
min_x_var  = 1e10
min_y_var  = 1e10

for t in range( max( WIDTH, HEIGHT ) ):
    x_pos = [(x + t * vx) % WIDTH  for x, vx in x_movement]
    y_pos = [(y + t * vy) % HEIGHT for y, vy in y_movement]
    x_var = variance(x_pos)
    y_var = variance(y_pos)

    if x_var < min_x_var:
        min_x_var = x_var
        step_x    = t

    if y_var < min_y_var:
        min_y_var = y_var
        step_y    = t 

second = step_x+((pow(WIDTH, -1, HEIGHT)*(step_y-step_x)) % HEIGHT)*WIDTH

print(second)
