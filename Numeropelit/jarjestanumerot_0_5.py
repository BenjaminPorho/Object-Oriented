# -*- coding: utf-8 -*-
"""

"""
from random import randint


class JarjestaNumerotPeli:
    def __init__(self, original: tuple):
        '''
        original on immutable tuple esim.  0,1,2,... or A, B, C...
        '''
        self.vertaa = original
        self.numerot = list(self.vertaa)

    @property
    def vertaa(self):
        return self.__vertaa

    @vertaa.setter
    def vertaa(self, original):
        if type(original) != tuple:
            self.__vertaa = tuple(original)
        else:
            self.__vertaa = original

    @property
    def numerot(self):
        return self.__numerot

    @numerot.setter
    def numerot(self, list):
        self.__numerot = list
        while True:
            self.__sekoita()
            if self.__onkoratkaistavissa():
                break

    def onkovalmis(self):
        '''
        vertaa vastaako järjestetty lista vertaa tuplea
        '''
        return tuple(self.numerot) == self.vertaa

    def move(self, valinta):
        ''' varmistaa, että käyttäjän valinta on kelvollinen ja tekee siirron '''
        while True:
            if valinta in self.numerot:
                valinta = self.numerot.index(valinta)
                tyhja = self.numerot.index('_')
                # valinta ja tyhja samalla rivilä tai sarakkeessa vierekkäin
                if abs(valinta - tyhja) == 1 and (valinta // 3) == (tyhja // 3) or abs(valinta - tyhja) == 3 and \
                        valinta % 3 == tyhja % 3:
                    self.numerot[tyhja], self.numerot[valinta] = self.numerot[valinta], self.numerot[tyhja]
                    break

    def __onkoratkaistavissa(self):
        '''tarkistaa onko järjestys ratkaistavissa'''
        inversions = 0;
        for i in range(8):
            for j in range(i + 1, 8):
                if self.vertaa.index(self.numerot[i]) > self.vertaa.index(self.numerot[j]):
                    inversions += 1
        return inversions % 2 == 0

    def __sekoita(self):
        '''sekoita the order of numerot'''
        for i in range(1, 9):
            index = randint(0, i - 1)
            if index != i - 1:
                self.numerot[i - 1], self.numerot[index] = self.numerot[index], self.numerot[i - 1]

    def __str__(self):
        '''palauttaa numrot sisällön 3*3 taulukossa'''
        result = ''
        for i, var in enumerate(self.numerot):
            result += var
            result += '\n' if (i + 1) % 3 == 0 else ' '  # lyhyt if-else
        return result


def luo(sisalto=True):
    '''
    luo ja paluattaa listan 8 + tyhja
    sisalto=True 0, 1, ...
    sisalto=False 'A, 'B, ...
    '''
    numerot = []
    for i in range(1, 9):
        if sisalto:
            numerot.append(str(i))
        else:
            numerot.append(chr(i + 64))  # ASCII'A'
    numerot.append('_')
    return numerot


def main():
    '''varsinainen ohjelma'''
    peli = JarjestaNumerotPeli(luo(False))
    print(peli.vertaa)

    # the main loop
    while True:
        if peli.onkovalmis():
            print('Hyvää työtä!')
            break
        else:
            peli.move(input('siirrettävä alkio: ').upper())


if __name__ == '__main__':
    main()




