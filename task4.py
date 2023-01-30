from task2 import jainsall
# Oppgave 5. Task 4

my_file = open("task4.txt") # Read from file
        
my_list = []        # Opprett en liste

for each_line in my_file:
    input = each_line.strip("\n").split(" ")    # Split each line and take care of the number + the measurement
    number = int(input[0])
    measurement = input[1]

    # Sjekk om det er Kbps eller Mbps
    if measurement == 'Kbps':
        number = number / 100 # / 100 if it is Kpbs

    my_list.append(number) # Add to our list
    

print(jainsall(my_list))