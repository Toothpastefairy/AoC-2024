import re
from collections import defaultdict

f              = open ( "2024\\day5.txt" , "r" )
codes, updates = f.read ().split("\n\n")
codes   = [[int(i) for i in re.findall(r"\d+", code  )] for code   in codes.  splitlines()]
updates = [[int(i) for i in re.findall(r"\d+", update)] for update in updates.splitlines()]

ordeneded_dict = defaultdict(list)

for a, b in codes:
    ordeneded_dict[b].append(a)


count = 0
count_p2 = 0
for update in updates:

    correct = True
    for i in range(len(update)):
        for j in range(i, len(update)):
            code_left  = update[i]
            code_right = update[j]

            if code_right in ordeneded_dict[code_left]:
                correct = False
                break
        
        if not correct:
            break

    if correct:
        count += update[len(update)//2]

    while not correct:
        correct = True
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[j] in ordeneded_dict[update[i]]:
                    update[i], update[j] = update[j], update[i]
                    correct = False

        if correct:
            count_p2 += update[len(update)//2]


print ( "### PART 1 ###" )
print ( count            )

print ( "### PART 2 ###" )
print ( count_p2         ) 



