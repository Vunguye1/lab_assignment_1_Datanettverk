# Oppgave 2. Task 1

def jains(value1, value2):
    N = value2 - value1 + 1 # total number of flows
    sum = 0
    square_sum = 0
    
    for i in range(value1,value2+1):
        sum += i        # summary of every number
    

    for i in range(value1,value2+1):
        square_sum += i**2  # summary of every square number

    upperPart = sum**2      # square of sum
    belowPart = (N * square_sum) # total number of flow x summary of every square number

    JFI = upperPart / belowPart
    
    return JFI

print(jains(1,5))