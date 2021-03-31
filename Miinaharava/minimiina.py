'''
@author: Benjamin Pörhö, Oskari Toivanen, Joona Pääkkönen, Jesperi Vainio
minimiina.py
Miinaharavan gui.
'''

import tkinter as tk
import random
from functools import partial


class MiniMiina(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Minimiina-peli")
        self.geometry("500x500")

        self.luoLayout()

    def onClick(self, id_i, id_j):

        print(f'Valittuna {id_i}, {id_j}')
    

    def luoLayout(self):
        self.buttons = []
        self.button_ids = []

        #Luodaan 10x10 nappula-ikkuna.
        for i in range(10):
            self.columnconfigure(i, pad=3)
        
        for i in range(10):
            self.rowconfigure(i, pad=3)

        for i in range(10):
            for j in range(10):
                self.buttons = tk.Button(self, text="*", height=2, width=4, command=partial(self.onClick, i, j))
                self.button_ids.append(self.buttons)
                self.buttons.grid(row=i,column=j)




if __name__ == "__main__":
    MiniMiina().mainloop()