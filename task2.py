# Oppgave 3. Task 2
def jainsall(data):
    N = len(data) # total number of flows

    upperPart = sum(data)**2 # summary of every number. Then we square it

    square_numbers = 0
    for i in data:
        square_numbers += i**2  # same as task1

    belowPart = square_numbers * N

    return upperPart / belowPart #JFI

data = [1, 2, 3, 4, 5]

print(jainsall(data))