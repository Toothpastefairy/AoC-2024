f     = open ( "2024\\day16.txt" , "r" )
lines = f.read().splitlines()

HEIGHT     = len(lines) 
WIDTH      = len(lines[0])
DIRECTIONS = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]
DIR_SCORE  = {complex(  0, -1 ):     0,
              complex(  1,  0 ): 10000,
              complex(  0,  1 ): 20000, 
              complex( -1,  0 ): 30000 }

maze      = {}
start_pos = complex(0, 0)
end_pos   = complex(0, 0)

for b in range( HEIGHT ):
    for a in range( WIDTH ):
        cell       = complex( a, b )
        maze[cell] = lines[b][a]

        if maze[cell] == "S":
            start_pos = cell
            maze[cell] = "."
        if maze[cell] == "E":
            end_pos = cell
            maze[cell] = "."


def shouldAdd(paths, pos, dir, score):
    if not (pos, dir) in paths:
        return True
    
    return score < paths[(pos, dir)]


paths     = {(start_pos, complex(1,0)): 0}
positions = [(start_pos, complex(1,0))]


while positions:
    pos, original_dir = positions.pop()
    score = paths[(pos, original_dir)]

    for dir in [1, 1j, -1j]:
        new_dir   = original_dir * dir
        new_pos   = pos + new_dir
        new_score = score + 1 if new_dir == original_dir else score + 1001

        if maze[new_pos] != "#" and shouldAdd(paths, new_pos, new_dir, new_score):
            paths[(new_pos, new_dir)] = new_score
            positions.append((new_pos, new_dir))


min_score = 1e10
min_dir   = complex(0, 0)
for dir in DIRECTIONS:
    if (end_pos, dir) in paths:
        if paths[(end_pos, dir)] < min_score:
            min_dir   = dir
            min_score = paths[(end_pos, dir)]
        
print(min_score)

tiles = set([end_pos])
positions = [(end_pos, min_dir)]
while positions:
    pos, original_dir = positions.pop()
    score = paths[(pos, original_dir)]

    for dir in [1, 1j, -1j]:
        new_dir   = original_dir * dir
        new_pos   = pos - original_dir
        new_score = score -1 if new_dir == original_dir else score - 1001

        if (new_pos, new_dir) in paths:
            if paths[(new_pos, new_dir)] == new_score:
                positions.append((new_pos, new_dir))
                tiles.add(new_pos)


    if paths[(pos, original_dir)] == 0:
        continue

print(len(tiles))