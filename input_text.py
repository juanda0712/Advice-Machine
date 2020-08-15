import pygame as pg
from constants import *
'''
Clase Input;
- Maneja la entrada de teclado
        Funciones:
        1) keys: detecta el teclado y agrega las acciones a una lista
        E: Los eventos de teclado
        S: Una lista con los elementos que se ingresaron por teclado

        2) message: Dibuja la lista que genera la funcion keys 
        E: Pantalla , pos X y Y

'''
class Input:
    def __init__(self):
        self.lines = 0
        self.characters = ['',]
        self.font = pg.font.Font(None,25)
        self.distance = 20
        self.count = 0

    def keys(self,event):

        
        for action in event:
            if action.type == pg.KEYDOWN:
                if action.key == pg.K_BACKSPACE:
                    if self.characters[self.lines] == '' and self.lines > 0: 
                        self.characters == self.characters[0:-1]
                        self.lines -= 1
                        self.count -= 1
                    else:
                        self.count -= 1
                        self.characters[self.lines] = self.characters[self.lines][0:-1]
                elif self.count <24 :
                    self.count +=1
                    self.characters[self.lines] = str(self.characters[self.lines] + action.unicode)
                    

    def message(self,screen,posX,posY):
        self.posX = posX
        self.posY = posY
        for self.lines in range(len(self.characters)):
            letter = self.font.render(self.characters[self.lines],True,GOLD)
        screen.blit(letter,(self.posX,self.posY+self.distance*self.lines))