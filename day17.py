import re

f                       = open ( "2024\\day17.txt" , "r" )
registers, INSTRUCTIONS = f.read().split("\n\n")

registers    = [ int(i) for i in re.findall(r"\d+", registers   ) ]
INSTRUCTIONS = [ int(i) for i in re.findall(r"\d+", INSTRUCTIONS) ]


def getComboOperand(number, registers):
   if number in range(0, 4):
      return number
   if number in range(4, 7):
      return registers[number-4]
   
   return 0


def checkProgram(registers):
    output  = []
    pointer = 0
    
    while pointer < len(INSTRUCTIONS) - 1:
        opcode = INSTRUCTIONS[pointer]
        number = INSTRUCTIONS[pointer + 1]

        if   opcode == 0:
            registers[0] = registers[0] // (2**getComboOperand(number, registers))

        elif opcode == 1:
            registers[1] = registers[1] ^ number

        elif opcode == 2:
            registers[1] = getComboOperand(number, registers) % 8

        elif opcode == 3:
            if registers[0] != 0:
                pointer = number
                continue

        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]

        elif opcode == 5:
            addition = getComboOperand(number, registers) % 8
            output.append( addition )

        elif opcode == 6:
            registers[1] = registers[0] // (2**getComboOperand(number, registers))

        elif opcode == 7:
            registers[2] = registers[0] // (2**getComboOperand(number, registers))

        pointer += 2

    return output


output = checkProgram(registers)
print(",".join([str(i) for i in output]))

numbers = [0]
for length in range(1, len(INSTRUCTIONS) + 1):
    possible = []
    
    for num in numbers:
        for offset in range(8):
            a = offset + num * 8
            registers = [a, 0, 0]
            output    = checkProgram(registers)

            if output == INSTRUCTIONS[-length:]:
                possible.append(a)

    numbers = possible

print(min(numbers))