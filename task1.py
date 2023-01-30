# Oppgave 2. Task 1

def jains(value1, value2):
    N = value2 - value1 + 1 # total number of flows
    sum = 0
    square_sum = 0
    
    for i in range(value1,value2+1):
        sum += i
    

    for i in range(value1,value2+1):
        square_sum += i**2

    upperPart = sum**2
    belowPart = (N * square_sum)

    JFI = upperPart / belowPart

    return JFI

print(jains(1,5))