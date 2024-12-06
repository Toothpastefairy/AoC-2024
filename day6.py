f     = open ( "2024\\day6.txt" , "r" )
lines = f.read().splitlines()

maze        = dict()
maze_height = len(lines)
maze_width  = len(lines[0])

start_position  = complex(0, 0)
start_direction = complex(0, 0)

DIRECTIONS = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]

for b in range(maze_height):
    for a in range(maze_width):

        entity = lines[b][a]
        if (entity != ".") and (entity != "#"):
            start_position       = complex(a, b)
            maze[start_position] = "."

        match (entity):
            case "^":
                start_direction = 0
            case ">":
                start_direction = 1
            case "v":
                start_direction = 2
            case "<":
                start_direction = 3
            case _:
                maze[complex(a, b)] = entity


def checkMaze(maze, position, direction):

    visited = set()
    looping = set()

    while True:
        
        visited.add(position)
        looping.add((position, direction))

        next_position = position + DIRECTIONS[direction]
        next_tile     = maze.get(next_position)

        if ((next_position, direction)) in looping:
            return None

        if not next_tile:
            break
        elif next_tile == "#":
            direction = (direction + 1) % 4
        else:
            position += DIRECTIONS[direction]

    return visited


original_visited = checkMaze(maze, start_position, start_direction)

print ( "### PART 1 ###"        )
print ( len( original_visited ) )

causes_loops = 0
for place in original_visited:
    copied_maze = maze.copy()

    copied_maze[place] = "#"

    if not checkMaze(copied_maze, start_position, start_direction):
        causes_loops += 1

print ( "### PART 2 ###" )
print ( causes_loops     )
