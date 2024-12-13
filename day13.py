import re
from collections import defaultdict

f        = open ( "2024\\day13.txt" , "r" )
machines = [machine.splitlines() for machine in f.read().split("\n\n")]

a_buttons = []
b_buttons = []
prizes_p1 = []
prizes_p2 = []

for machine in machines:
    x, y = [int( i ) for i in re.findall(r"\d+",machine[0])]
    a_buttons.append(complex(x, y))

    x, y = [int( i ) for i in re.findall(r"\d+",machine[1])]
    b_buttons.append(complex(x, y))

    x, y = [int( i ) for i in re.findall(r"\d+",machine[2])]
    prizes_p1.append(complex(x, y))

    x += 10000000000000
    y += 10000000000000

    prizes_p2.append(complex(x, y))


def tokenAmount(a, b):
    return 3 * a + b


def isWhole(f, eps):
    return abs(f - round(f)) < abs(eps)


total_tokens = 0
for id in range(len(machines)):
    tokens = 1e10

    a_button = a_buttons[id]
    b_button = b_buttons[id]
    prize    = prizes_p1[id]

    # key is position, value is button presses => info to calc token amount
    for i in range(100):
        for j in range(100):
            grid_pos = i * a_button + j * b_button

            if grid_pos == prize:
                new_tokens = tokenAmount(i, j)
                tokens = new_tokens if new_tokens < tokens else tokens

    if tokens != 1e10:
        total_tokens += tokens


print(total_tokens)

total_tokens = 0
for id in range(len(machines)):
    tokens = 1e10

    a = a_buttons[id]
    b = b_buttons[id]
    p = prizes_p2[id]

    denominator = a.imag - (a.real * b.imag / b.real)
    numerator   = p.imag - (p.real * b.imag / b.real)

    a_presses = numerator / denominator
    b_presses = (p.real - (a_presses * a.real)) / b.real

    if isWhole(a_presses, 1e-3) and isWhole(b_presses, 1e-3):
        total_tokens += tokenAmount(a_presses, b_presses)

print(int(total_tokens))