# -*- coding: utf-8 -*-
'''
@author: Benjamin Pörhö
nopat.py
'''

"""
Tupla-tai-kuitti-noppapeli

Käyttäjä asettaa panoksen, joka on välillä 1 - potti. Potti on alussa 100.
Ohjelma heittää nopar, tarkistaa tuloksen, laskee voiton/tappion, 
päivittää potin ja näyttää sen käyttäjälle.
Jos potti on suurempi kuin 0 peli jatkuu seuraavalle kierrokselle. 
Jos pelaaja lopettaa pelin ennen kuin potti on kulunut, pottia ei tallenneta 
(pelaaja voi muuttaa sen rahaksi kasinon pankissa) 
Lisätty toiminnallisuus tenner, joka kymmenkertaistaa panoksen ennen heittoa, ja jos heitettyjen noppien summa on 10 lisää pottiin 10*(10*panos)
"""

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk #basic Tk widgets are overriden
from peli import Peli
from tiedostohandler import TiedostoHandler
import tkinter.filedialog as tf

from abc import ABC, abstractmethod

class Tenner(ABC):
    @abstractmethod
    def tenner(self):
        pass    

class Nopat(Tenner, tk.Tk) :
    '''
    kahden nopan noppapeli, jolla on Tk-GUI
    '''
    #Luodaan peli-luokka tyyppinen attribuutti luokalle Nopat
    peli = Peli()

    ##############################tenner######################
    def tenner(self):
        if self.selectvalue.get():
             self['bg']='yellow'
             self.title('Tupla tai kuitti - Tenner')
        else:
             self['bg']='lightgray'
             self.title('Tupla tai kuitti')
    ##########################################################

    
    def __init__(self, *args, **kwargs ) :

        super().__init__(*args, **kwargs) # Tk class init
        self.title('Tupla tai kuitti')
        self.geometry('460x160')
        self.peli.potti = int(TiedostoHandler().lue("teksti.txt"))
        self.luoLayout()

        self.protocol("WM_DELETE_WINDOW", self.close)

    def luoLayout(self):
        '''luo widgetit ja asettele ne gridiin'''
        self.__v_panos = tk.IntVar()
        self.__v_panos.set(1)
        self.__v_heitto = tk.StringVar(value='Heitä')
        self.__tulos = tk.StringVar()
        self.__tulos.set(f'Alkupotti on {self.peli.potti}')
        self.__error = tk.StringVar()
        self.__error.set('')
         
        self.columnconfigure(0, weight = 1)
        self.__l_panos = ttk.Label( self, text = 'Aseta panos', justify = tk.CENTER)
        self.__l_panos.grid(sticky = tk.N + tk.S)
        self.__e_panos = ttk.Entry( self, textvariable = self.__v_panos, justify = tk.CENTER)
        self.__e_panos.grid(sticky = tk.N + tk.S)
 
        self.b = ttk.Button(self, textvariable = self.__v_heitto, command=self.__rollandcheck)
        self.b.grid(sticky = tk.N + tk.S)
        ttk.Label( self, textvariable=self.__tulos, anchor = tk.CENTER ).grid(sticky = tk.NSEW)
        ttk.Label( self, textvariable=self.__error, anchor = tk.CENTER ).grid(sticky = tk.N + tk.S)

        ##############################tenner######################
        self.selectvalue = tk.IntVar()
        self.checkb = ttk.Checkbutton( self, text="Tenner", variable=self.selectvalue, 
                 onvalue = 1, offvalue = 0, command=self.tenner)
        self.checkb.grid(sticky = tk.N + tk.S)	
        self.tenner()
        ##############################tenner######################


    def __rollandcheck(self):
        '''nappulan komento, heittää, tarkistaa ja näyttää tuloksen'''
        try:
            self.__error.set('')
            self.peli.panos = self.__v_panos.get()
            self.peli.roll()
            ##############################tenner######################
            panos = self.peli.panos * 10 #noudatetaan ehtoa panos = [1..potti] 
            if self.selectvalue.get():
                if sum(self.peli.luku) == 10:
                    self.peli.potti = self.peli.potti + panos*10 #päivitetään potti tennered panoksella
                    self.__tulos.set(f'{self.peli.luku[0]} ja {self.peli.luku[1]} summa on 10! Voitit panoksesi ({self.peli.panos} x 10) 10-kertaisesti potti on {self.peli.potti}')
                else: #panos on tennered, mutta muuten tarkistus normaali, ja perään korjaus potissa ja                     
                    alkupotti = self.peli.potti #alkupottiturvaan ennen tarkistusta
                    self.peli.tarkista() #takistusalkuperäisellä panoksella
                    loppupotti = self.peli.potti #potti, jos panos on alkuperäinen                
                    kerroin = (loppupotti - alkupotti) // self.peli.panos #mikä oli kerroin, jolla panos pottiin lisättiin
                    self.peli.potti = alkupotti + kerroin * panos #tennered panoksen kanssa potin laskenta
                    tilanneteksti1 = "voitit " if kerroin > 0 else "hävisit "
                    tilanneteksti2 = "" if (kerroin == 0 or abs(kerroin) == 1) else f'{abs(kerroin)}-kertaisesti'
                    self.__tulos.set(f'{self.peli.luku[0]} ja {self.peli.luku[1]} - {tilanneteksti1} panoksen ({self.peli.panos} x 10) {tilanneteksti2}. Potti on nyt {self.peli.potti}')
            ##########################################################
            else:  #sama kuin aiemmin ilman tenneriä      
                self.__tulos.set(self.peli.tarkista())
            if self.peli.potti <= 0 : 
                self.title('Potti on kulutettu - peli on pelattu!')
                self.__l_panos.grid_remove() #poistaa, mutta muistaa asetukset
                self.__e_panos.grid_remove()
                self.b.grid_remove()
                self.checkb.grid_remove()
                if messagebox.askyesno('Haluatko aloittaa alusta?', 'Sinun on sijoitettava uusi alkupotti ensin'):
                    self.title('Tupla tai kuitti')
                    self.peli.potti = 100
                    self.__tulos.set(f'Alkupotti on {self.peli.potti}')
                    self.peli.panos = 1
                    self.__v_panos.set(self.peli.panos)               
                    self.__l_panos.grid() #palauttaa asetuksineen
                    self.__e_panos.grid()
                    self.b.grid()
                    self.checkb.grid()
                    ##############################tenner######################
                    self.selectvalue.set(0)
                    self.tenner()
                    ##########################################################
                else:
                    self.destroy()
        except ValueError as error:
            self.__error.set(error)
            self.__v_panos.set(self.peli.panos)
            self.__tulos.set('')

    def close(self):
        '''
        called when the window closing cross is selected
        asks if user wants to save first 
        yes = ture, no = false, cancel = None
        '''
        TiedostoHandler().kirjoita("teksti.txt", str(self.peli.potti))
        print(self.peli.potti)
        self.destroy()

    
if __name__ == '__main__' :
    Nopat().mainloop()

