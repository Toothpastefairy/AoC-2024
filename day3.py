import re

f     = open ( "2024\\day3.txt" , "r" )
line  = f.read ().replace( "\n", "" )


total_result = 0

for i, j in re.findall(r'mul\((\d+),(\d+)\)', line):
    total_result += int(i) * int(j)

print ( "### PART 1 ###" )
print ( total_result     )


total_result = 0

line = re.sub(r"(don't\(\))(.*?)(do\(\))", "", line)
line = re.sub(r"(don't\(\))(.*)"         , "", line)

for i, j in re.findall(r'mul\((\d+),(\d+)\)', line):
    total_result += int(i) * int(j)

print ( "### PART 2 ###" )
print ( total_result     )