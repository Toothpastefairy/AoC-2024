f               = open ( "2024\\day15.txt" , "r" )
inp, movements = f.read().split("\n\n")

inp = inp.splitlines()

HEIGHT     = len(inp) 
WIDTH      = len(inp[0])
DIRECTIONS = { ">": complex(  1,  0 ),
               "v": complex(  0,  1 ),
               "<": complex( -1,  0 ),
               "^": complex(  0, -1 ) }

movements = list(movements.replace("\n", ""))
maze      = {}

start_pos = complex(0, 0)

for b in range(HEIGHT):
    for a in range(WIDTH):
        pos = complex(a, b)
        maze[pos] = inp[b][a]

        if maze[pos] == "@":
            start_pos = pos
            maze[pos] = "."


def findDepth ( pos, dir, maze ):
    depth = 0
    while True:
        pos = pos + dir

        if   maze[pos] == "#":
            return -1
        elif maze[pos] == "O":
            depth += 1
        else:
            return depth
        

pos = start_pos
for move in movements:
    dir   = DIRECTIONS[move]
    depth = findDepth ( pos, dir, maze )

    if depth == -1:
        continue

    pos = pos + dir
    maze[pos], maze[pos + dir*depth] = maze[pos + dir*depth], maze[pos]

total_gps = 0
for b in range(HEIGHT):
    for a in range(WIDTH):
        p = complex(a, b)
        if maze[p] == "O":
            total_gps += round(p.real + p.imag * 100)
        if p == pos:
            print("@", end='', sep='')
        else:
            print(maze[p], end='', sep='')
    print()

print(total_gps)


# Part 2
maze      = {}
start_pos = complex(0, 0)

for b in range(HEIGHT):
    for a in range(WIDTH):
        pos1 = complex(2*a, b)
        pos2 = complex(2*a+1, b)
        maze[pos1] = inp[b][a]
        maze[pos2] = inp[b][a]

        if maze[pos1] == "@":
            start_pos = pos1
            maze[pos1] = "."
            maze[pos2] = "."

        if maze[pos1] == "O":
            maze[pos1] = "["
            maze[pos2] = "]"

        
for b in range(HEIGHT):
    for a in range(2*WIDTH):
        p = complex(a, b)
        if p == start_pos:
            print("@", end='', sep='')
        else:
            print(maze[p], end='', sep='')
    print()


pos = start_pos
for move in movements:
    dir   = DIRECTIONS[move]
    
    # depth structure {depth level: cells in layer}
    depth = 0
    structure = {depth: set([pos])}

    # vertical movement
    
    while True:
        structure[depth + 1] = set()

        no_block = True
        for cell in structure[depth]:
            next_cell = cell + dir

            if   maze[next_cell] == "#":
                depth = -1
                break

            elif maze[next_cell] == "[":
                structure[depth + 1].add(next_cell)
                no_block = False
                if dir.imag != 0:
                    structure[depth + 1].add(next_cell + complex(  1, 0 ) )
                
            elif maze[next_cell] == "]":
                structure[depth + 1].add(next_cell)
                no_block = False
                if dir.imag != 0:
                    structure[depth + 1].add(next_cell + complex( -1, 0 ) )
            
        if no_block or (depth == -1):
            break

        depth += 1
    
    if depth == -1:
        continue

    for i in reversed(range(depth+1)):
        for cell in structure[i]:
            maze[cell], maze[cell + dir] = maze[cell + dir], maze[cell]

    pos += dir

total_gps = 0
for b in range(HEIGHT):
    for a in range(2*WIDTH):
        p = complex(a, b)
        if maze[p] == "[":
            total_gps += round(p.real + p.imag * 100)
        if p == pos:
            print("@", end='', sep='')
        else:
            print(maze[p], end='', sep='')
    print()

print(total_gps)