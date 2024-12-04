f    = open ( "2024\\day4.txt" , "r" )
GRID = [list(i) for i in f.read().splitlines()]

GRID_HEIGHT = len(GRID)
GRID_WIDTH  = len(GRID[0])

LETTERS = "XMAS"
neighbours = [[-1, -1],[ 0, -1],[ 1, -1],[-1,  0],
              [ 1,  0],[-1,  1],[ 0,  1],[ 1,  1]]


count = 0

def checkXmas(i, j, neighbour, depth):
    ret = False

    if i < 0 or i >= GRID_HEIGHT:
        return False
    if j < 0 or j >= GRID_WIDTH:
        return False
    
    if LETTERS[depth] == GRID[i][j]:
        if depth == 3:
            return True
        else:
            i += neighbour[0]
            j += neighbour[1]

            ret = checkXmas( i, j, neighbour, depth + 1 )

    return ret

for i in range(GRID_HEIGHT):
    for j in range(GRID_WIDTH):
        for neighbour in neighbours:
            count += checkXmas(i, j, neighbour, 0)

print ( "### PART 1 ###" )
print ( count            )


count = 0

for i in range( 1, GRID_HEIGHT - 1 ):
    for j in range( 1, GRID_WIDTH - 1 ):
        if GRID[i][j] != "A":
            continue

        string1 = GRID[i-1][j-1] + GRID[i][j] + GRID[i+1][j+1]
        string2 = GRID[i-1][j+1] + GRID[i][j] + GRID[i+1][j-1]

        if (string1 == "SAM" or string1 == "MAS") and \
           (string2 == "SAM" or string2 == "MAS"):

           count +=1

print ( "### PART 2 ###" )
print ( count ) 

