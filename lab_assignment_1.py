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
print(jains(1,5))
print(jainsall(data))


# Oppgave 4. Task 3

min_fil = open("task3.txt")
        # Opprett en liste
input_liste = []
for hver_linje in min_fil:
    input = hver_linje.split(" ")
    input_liste.append(int(input[0]))
    

print(jainsall(input_liste))

# Oppgave 5. Task 4

my_file = open("task4.txt")
        # Opprett en liste
my_list = []

for each_line in my_file:
    input = each_line.strip("\n").split(" ")
    number = int(input[0])
    measurement = input[1]

    # Sjekk om det er Kbps eller Mbps
    if measurement == 'Kbps':
        number = number / 100

    my_list.append(number)
    

print(jainsall(my_list))