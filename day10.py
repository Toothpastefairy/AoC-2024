f     = open ( "2024\\day10.txt" , "r" )
lines = f.read().splitlines()

maze        = dict()
maze_height = len(lines)
maze_width  = len(lines[0])

DIRECTIONS = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]

for b in range( maze_height ):
    for a in range( maze_width ):
        cell = complex( a, b )
        maze[cell] = int( lines[b][a] )

score_p1 = 0
for trailhead, start in maze.items():
    if start != 0:
        continue

    possible_paths = set( [trailhead] )
    for i in range( 9 ):
        next_paths = set()

        for pos in possible_paths:
            for dir in DIRECTIONS:

                if maze.get( pos+dir ) == i+1:
                    next_paths.add( pos+dir )

        possible_paths = next_paths.copy()

    score_p1 += len( possible_paths )

print( score_p1 )


score_p2 = 0
for trailhead, start in maze.items():
    if start != 0:
        continue

    possible_paths = [trailhead]
    for i in range(9):
        next_paths = []

        for pos in possible_paths:
            for dir in DIRECTIONS:

                if maze.get( pos+dir ) == i+1:
                    next_paths.append( pos+dir )

        possible_paths = next_paths.copy()

    score_p2 += len( possible_paths )

print(score_p2)