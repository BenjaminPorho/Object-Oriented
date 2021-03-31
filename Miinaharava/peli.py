'''
@author: Benjamin Pörhö, Oskari Toivanen, Joona Pääkkönen, Jesperi Vainio
peli.py
Miinaharavan toiminnallisuus.
'''

from abc import ABC, abstractmethod

class IPelit(ABC):


    @abstractmethod
    def siirra(self, parametri):
        pass

    @abstractmethod
    def onkoValmis(self):
        pass

    @abstractmethod
    def uusiPeli(self):
        pass

