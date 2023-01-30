from task2 import *
# Oppgave 4. Task 3 

min_fil = open("task3.txt") # Read from file
        # Opprett en liste
input_liste = []
for hver_linje in min_fil: #For each line in 4 lines we have
    input = hver_linje.split(" ") # Split each line into 2 different variables
    input_liste.append(int(input[0]))   # Only take the number and add to the list
    

print(jainsall(input_liste))