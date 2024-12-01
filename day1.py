import re

f     = open ( "2024\\day1.txt" , "r" )
lines = f.read () .splitlines ()

left_list  = []
right_list = []

for line in lines:
    left_value, right_value = [int(i) for i in re.findall(r'\d+', line)]

    left_list .append ( left_value )
    right_list.append ( right_value )

left_list .sort ()
right_list.sort ()

total_difference = 0

for i in range(len(left_list)):
    total_difference += abs(left_list[i] - right_list[i])

print ( "### PART 1 ###" )
print ( total_difference )

# part 2

similarity_score = 0
ri               = 0  # right index

for li in range(len(left_list)):
    left_value = left_list[li]

    count = 0
    while (right_list[ri] <= left_value) and (ri < len(right_list)):
        if right_list[ri] == left_value:
            count += 1

        ri += 1

    similarity_score += left_value * count
    
print ( "### PART 2 ###" )
print ( similarity_score )