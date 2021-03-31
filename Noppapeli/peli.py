'''
@author: Benjamin Pörhö
peli.py
'''

import random


class Peli():
    
    def __init__(self, potti=100, panos=1, maara=2, *args, **kwargs) :
        
        self.potti = potti 
        self.panos = panos
        self.maara = maara
        self.luku = [0]*maara    

    @property
    def potti(self):
        return self.__potti
    
    @potti.setter
    def potti(self, potti):
        '''
        pakottaa potti >= 0
        '''
        self.__potti = potti
        if self.__potti < 0 : self.__potti = 0
    
    @property
    def panos(self):
        return self.__panos
    
    @panos.setter
    def panos(self, panos):
        '''
        asettaa panos [1, potti]
        '''
        if panos >= 1 and panos <= self.potti :
            self.__panos = panos
        else :
            raise ValueError(f'panos on oltava 1..{self.potti}')
   
    @property
    def maara(self):
        return self.__maara
    
    @maara.setter
    def maara(self, maara):
        '''
        asettaa noppien määrän > 0
        '''
        if maara > 0:
            self.__maara = maara
            self.luku = [0]*maara
    
    def roll(self) : 
        '''
        täyttää luvut listan satunnaisilla nopan silmäluvuilla [1,6]
        '''
        for i in range(self.maara) :
            self.luku[i] = random.randint(1, 6)
    
    def tarkista(self):
        '''
        tupla-tai-kuitti jos kahden nopan silmäluvut ovat:
            * tupla 1 tai 6 käyttäjä voittaa panoksen kymmenkertaisena (panos*10)
            * tupla 2, 3, 4, tai 5 käyttäjä voittaa panoksen tuplana (panos*2)
            * ei tuplaa tai summa on 6 käyttäjä menettää panoksen
            * muut yhdistelmät (ei tuplaa, summa eri kuin 6) käyttäjä häviää panoksen tuplana (panos*(-2))  
        Voitto (päivitetty panos) lisätään ja  hävitty panos vähennetään potista.
        '''
        text = f'{self.luku[0]} and {self.luku[1]} - You '
        if self.maara != 2 :
            raise ValueError('Väärä peli, tupla-tai-kuitti on kahden nopan peli')
        else :
            if self.luku[0] == self.luku[1] :
                if self.luku[0] == 1 or self.luku[0] == 6 :
                    text += f'voitit {self.panos} x 10!'
                    self.potti += self.panos * 10
                else :
                    text += f'voitit {self.panos} x 2!'
                    self.potti += self.panos * 2
            elif sum(self.luku) == 6 :
                text += f'menetit {self.panos} panoksesi!'
            else :
                text += f'Hävisit {self.panos} x 2!'
                self.potti -= self.panos * 2
            text += f'\npotti on {self.potti}'
        return text