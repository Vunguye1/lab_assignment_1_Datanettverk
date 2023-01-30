from task2 import jainsall
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