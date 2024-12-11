from math import log10
from collections import defaultdict

f       = open ( "2024\\day11.txt" , "r" )
numbers = [int( i ) for i in f.read().split(" ")]

numbers = { number: 1 for number in numbers }

def determineNumbers( numbers, iterations ):

    for _ in range( iterations ):
        new_numbers = defaultdict( int )
        for number, count in numbers.items():
            
            if number == 0:
                new_numbers[1] += count
            else:
                digits = int( log10( number ) ) + 1

                if digits % 2 == 0:
                    first_half  = int( number // (10**(digits/2)) )
                    second_half = int( number %  (10**(digits/2)) )

                    new_numbers[first_half] += count
                    new_numbers[second_half] += count

                else:
                    new_numbers[2024 * number] += count

        numbers = new_numbers

    return sum( numbers.values() )


print( "### PART 1 ###"                )
print( determineNumbers( numbers, 25 ) )

print( "### PART 2 ###"                )
print( determineNumbers( numbers, 75 ) )