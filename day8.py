from collections import defaultdict

f       = open ( "2024\\day8.txt" , "r" )
grid    = f.read().splitlines()

GRID_LENGTH = len( grid    )
GRID_WIDTH  = len( grid[0] )


def isSpotLegal(spot):
    return spot.real >= 0 and spot.real < GRID_LENGTH and \
           spot.imag >= 0 and spot.imag < GRID_WIDTH


positions = defaultdict( list )

for i, line in enumerate( grid ):
    for j, char in enumerate( line ):
        if char == ".":
            continue

        positions[char].append( complex( j, i ) )

total_antinodes           = set()
total_antinodes_with_harm = set()

for key, value in positions.items():
    for i in range( len( value ) ):
        antenna1 = value[i]
        total_antinodes_with_harm.add(antenna1)

        for j in range( i + 1, len( value ) ):
            antenna2 = value[j]

            difference = antenna2 - antenna1
            spot1      = antenna1 - difference
            spot2      = antenna2 + difference

            if isSpotLegal ( spot1 ):
                total_antinodes.add( spot1 )

            if isSpotLegal ( spot2 ):
                total_antinodes.add( spot2 )

            while isSpotLegal ( spot1 ):
                total_antinodes_with_harm.add( spot1 )
                spot1 -= difference

            while isSpotLegal ( spot2 ):
                total_antinodes_with_harm.add( spot2 )
                spot2 += difference


print( "### PART 1 ###" )
print( len( total_antinodes ) )

print( "### PART 2 ###" )
print( len( total_antinodes_with_harm ) )