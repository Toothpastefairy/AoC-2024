from collections import defaultdict

f       = open ( "2024\\day12.txt" , "r" )
lines = f.read().splitlines()

garden        = dict()
garden_height = len(lines)
garden_width  = len(lines[0])

DIRECTIONS = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]

for b in range( garden_height ):
    for a in range( garden_width ):
        cell = complex( a, b )
        garden[cell] = lines[b][a]

total_price_p1 = 0
total_price_p2 = 0
visited        = set()

for b in range( garden_height ):
    for a in range( garden_width ):
        cell  = complex( a, b )
        plant = garden[cell]
        
        if cell in visited:
            continue
        
        visited.add(cell)
        neighbours = [cell]

        area      = 0
        perimiter = 0

        complex_perimiter = defaultdict(set)

        while neighbours:
            cell = neighbours.pop()

            area += 1

            for dir in DIRECTIONS:
                new_cell = cell + dir

                if (new_cell not in visited) and garden.get( new_cell ) == plant:
                    neighbours.append ( new_cell )
                    visited.   add    ( new_cell )
                elif garden.get( new_cell ) != plant:
                    perimiter += 1

                    complex_perimiter[cell].add(dir)

        sides_double_counted = 0
        for cell, dir_set in complex_perimiter.copy().items():
            for dir in dir_set:
                other_neighbour_1 = dir *  1j
                other_neighbour_2 = dir * -1j
                    
                sides_double_counted += (not dir in complex_perimiter[cell + other_neighbour_1])
                sides_double_counted += (not dir in complex_perimiter[cell + other_neighbour_2])
                        
        total_price_p1 += area * perimiter
        total_price_p2 += area * (sides_double_counted // 2)


print( "### PART 1 ###" )
print( total_price_p1   )

print( "### PART 1 ###" )
print( total_price_p2   )