import re

f     = open ( "2024\\day18.txt" , "r" )
lines = f.read().splitlines()

HEIGHT     = 71
WIDTH      = 71
DIRECTIONS = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]

start_pos = complex(0, 0)
end_pos   = complex(WIDTH - 1, HEIGHT - 1)


def isOutOfBounds(position):
    return ( position.real < 0 or position.real >= WIDTH  ) or \
           ( position.imag < 0 or position.imag >= HEIGHT )


def checkMaze(iterations, start_pos, end_pos, lines):
    positions = set([start_pos])
    visited   = set()
    blocked   = set()

    for i in range(iterations):
        a, b = [int(j) for j in re.findall(r"\d+", lines[i])]
        blocked.add(complex(a, b))

    i = 0
    while end_pos not in positions:
        i+= 1
        next_posistions = set()

        for pos in positions:
            for dir in DIRECTIONS:
                new_pos = pos + dir

                if new_pos not in visited and not isOutOfBounds(new_pos) and new_pos not in blocked:
                    visited        .add(new_pos)
                    next_posistions.add(new_pos)


        positions = next_posistions

        if len(positions) == 0:
            return -1

    return i


print(checkMaze(1024, start_pos, end_pos, lines))


for iteration in range(len(lines)):
    if checkMaze(iteration, start_pos, end_pos, lines) == -1:
        print(lines[iteration-1])
        break