f     = open ( "2024\\day2.txt" , "r" )
lines = f.read () .splitlines ()


def isReportSafe(numbers, rising):
    for i in range(1, len(numbers)):
        level_difference = numbers[i] - numbers[i-1]

        if ( (    rising) and (not (1  <= level_difference <= 3 )) ) or \
           ( (not rising) and (not (-3 <= level_difference <= -1)) ):
            return False
        
    return True


safe_reports    = 0
safe_reports_p2 = 0

for line in lines:
    numbers = [int(i) for i in line.split()]

    rising = numbers[1] > numbers[0]
    
    if isReportSafe(numbers, rising):
        safe_reports    += 1
        safe_reports_p2 += 1
    else:
        for i in range(len(numbers)):
            dampened_numbers = numbers[:i] + numbers[i+1:]
            rising           = dampened_numbers[1] > dampened_numbers[0]

            if isReportSafe(dampened_numbers, rising):
                safe_reports_p2 += 1
                break

    


print ( "### PART 1 ###" )
print ( safe_reports     )

print ( "### PART 2 ###" )
print ( safe_reports_p2  )