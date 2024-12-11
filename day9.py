f       = open ( "2024\\day9.txt" , "r" ).read()

blocks          = [ int(i) for i in f[::2]  ]
free_space      = [ int(i) for i in f[1::2] ] + [0]

disk_map = []

for i in range( len( blocks ) ):
    for _ in range( blocks[i] ):
        disk_map.append( i )

    for _ in range(free_space[i]):
        disk_map.append( None )

disk_map_p2 = disk_map.copy()

ri = len( disk_map ) - 1
for i in range( len( disk_map ) ):
    if ri <= i:
        break

    if disk_map[i] == None:
        disk_map[i], disk_map[ri] = disk_map[ri], disk_map[i]

    while disk_map[ri] == None:
        ri -= 1


disk_map = [x for x in disk_map if x is not None]

checksum = sum( i * value for i, value in enumerate( disk_map ) )

print( "### PART 1 ###" )
print( checksum         )


def blockLength( disk_map, index, reverse = 1 ):
    block_length = reverse

    while disk_map[index] == disk_map[index + block_length]:
        block_length += reverse

        if index + block_length < 0 or index + block_length >= len( disk_map ):
            break

    return abs( block_length )


disk_map = disk_map_p2

ri = len( disk_map ) - 1
while ri > 0:
    while disk_map[ri] == None:
        ri -= 1

    bl = blockLength( disk_map, ri, -1 )

    for i in range(0, ri):
        if disk_map[i] == None and blockLength( disk_map, i, 1 ) >= bl:
            disk_map[i:i+bl], disk_map[ri-bl+1:ri+1] = disk_map[ri-bl+1:ri+1], disk_map[i:i+bl]
            break

    ri -= bl


checksum_p2 = 0
for i in range( len( disk_map ) ):
    if disk_map[i] == None:
        continue

    checksum_p2 += i * disk_map[i]

print( "### PART 2 ###" )
print( checksum_p2 )
