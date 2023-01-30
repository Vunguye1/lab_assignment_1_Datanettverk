from task2 import *
# Oppgave 4. Task 3

min_fil = open("task3.txt")
        # Opprett en liste
input_liste = []
for hver_linje in min_fil:
    input = hver_linje.split(" ")
    input_liste.append(int(input[0]))
    

print(jainsall(input_liste))