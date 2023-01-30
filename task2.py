# Oppgave 3. Task 2
def jainsall(data):
    N = len(data)

    upperPart = sum(data)**2

    square_numbers = 0
    for i in data:
        square_numbers += i**2

    belowPart = square_numbers * N

    return upperPart / belowPart

data = [1, 2, 3, 4, 5]

print(jainsall(data))