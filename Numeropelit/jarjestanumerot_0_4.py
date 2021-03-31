"""
jarjestanumerot_0_4.py, neljäs vaihe järjestä numerot pelin toteuttamisesta.
@author: Benjamin Pörhö
"""
import random

def create():
    numbers = []
    for i in range (1,10):
        numbers.append(i)
    numbers.append("_")
    return numbers


def shuffle(numbers):
    random.shuffle(numbers)
    return numbers


def isItSolvable(numbers, compare):
    inversions = 0;
    for i in range(8):
        for j in range(i + 1, 8):
            if compare.index(numbers[i]) > compare.index(numbers[j]):
                inversions += 1
            elif inversions % 2 == 0:
                return ("Even is solvamble.")
            else:
                return ("Uneven isn't solvable.")


def isItReady(numbers, compare):
    if numbers == compare:
        print("You won the game!")


def scoreBoard(numbers):
    for i, var in enumerate(numbers):
        print(var) if (i + 1) % 3 == 0 else print(var, end=" ")


def move(numbers):
    while True:
        print("\n")
        n = input('Give an integer between 1 and 9: ')
        try:
            n = int(n)
            if n >= 1 and n <= 9:
                move = n
                break
            else:
                print('Give an integer between 1 and 9: ')
        except:
            print('You failed!')

    lindex = numbers.index(n)
    tindex = numbers.index("_")

    numbers[lindex], numbers[tindex] = numbers[tindex], numbers[lindex]

    return move

def main():
    numbers = create()
    compare = numbers
    compare = tuple(compare)

    print("Original order")
    for i, var in enumerate(compare):
        print(var) if (i + 1) % 3 == 0 else print(var, end=" ")
    print("\n")
    print("Solve the puzzle by moving the empty block: ")

    while True:
        shuffle(numbers)
        isItSolvable(numbers, compare)
        break


    while True:
        scoreBoard(numbers)
        if isItReady(numbers, compare):
            print("You won!")
            break
        else:
            move(numbers)

