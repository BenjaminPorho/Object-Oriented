"""
jarjestanumerot_0_3, kolmas vaihe järjestä numerot pelin toteuttamisesta.
@author: Benjamin Pörhö
tuodut moduulit: random
"""
import random

numbers = random.sample(range(1, 9), 8)
numbers.append("_")
compare = (1, 2, 3, 4, 5, 6, 7, 8, '_')

print("Järjestä numerot oikeean järjestykseen.")
empty = "_"

while tuple(numbers) != compare:
    for i, var in enumerate(numbers):
        print(var) if (i + 1) % 3 == 0 else print(var, end='')

    inversions = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if compare.index(numbers[i]) > compare.index(numbers[j]):
                inversions += 1
    try:
        empty = '_'
        move = int(input("Minkä numeron haluat vaihtaa tyhjän kanssa?: "))
        empty_index = numbers.index(empty)
        move_index = numbers.index(move)

        numbers[empty_index], numbers[move_index] = numbers[move_index], numbers[empty_index]

        if tuple(numbers) == compare:
            for i, var in enumerate(numbers):
                print(var) if (i + 1) % 3 == 0 else print(var, end='')
            print("Numerot ovat oikeassa järjestyksessä, voitit pelin!")
            break
    except ValueError:
        print("Anna kokonaisluku väliltä 1-8: ")
        continue