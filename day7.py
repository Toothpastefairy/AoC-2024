import re

f       = open ( "2024\\day7.txt" , "r" )
lines   = f.read().splitlines()
numbers = [[int( i ) for i in re.findall(r'\d+', line)] for line in lines]

calibrations = [row[0] for row in numbers]
measurements = [row[1:] for row in numbers]


def isCombined(should_be, result, to_check, also_concat):
    if len( to_check ) == 0:
        return should_be == result

    number = to_check.pop( 0 )

    result1 = result * number
    result2 = result + number
    ret1    = isCombined ( should_be, result1, to_check[:], also_concat )
    ret2    = isCombined ( should_be, result2, to_check[:], also_concat )
    ret3    = False

    if also_concat:
        result3 = int( str( result ) + str( number ) )
        ret3 = isCombined ( should_be, result3, to_check[:], also_concat )

    return (ret1 or ret2 or ret3)


total1 = 0
total2 = 0
for i in range( len( calibrations ) ):
    calibration = calibrations[i]
    measurement = measurements[i]

    if isCombined ( calibration, measurement[0], measurement[1:], False ):
        total1 += calibration

    if isCombined ( calibration, measurement[0], measurement[1:], True ):
        total2 += calibration

print ( "### PART 1 ###" )
print ( total1 )

print ( "### PART 2 ###" )
print ( total2 )