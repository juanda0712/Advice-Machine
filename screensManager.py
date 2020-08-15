import pygame as pg
from constants import *
from buttonsManager import *
from input_text import *
import random

'''
Clase Screen;
- Maneja las operaciones mas importantes del programa
        Funciones:
        1) draw: Maneja todas las pantallas de la maquina
        E: El estado de las 4 pantallas, pantalla principal, precio, dinero, eventos
        S: Pantalla que tenga el estado en True  

'''

class Screens():
    def __init__(self, screen):
        self.screen = screen
        self.input_text = Input()

    def __draw__(self, state_01, state_02, state_03, state_04, events, screens_manage,screens_buttons,type_img,num,price,money):
        self.state_01 = state_01
        self.state_02 = state_02
        self.state_03 = state_03
        self.state_04 = state_04
        self.type_img = type_img
        self.price = price
        self.money = money
        self.screens_manage  = screens_manage
        self.screens_buttons = screens_buttons
        
        if self.state_01:
            self.screens_buttons.create_buttons(TIPS, 405, 100, 150, 35, WHITE, GOLD, TIPS)
            self.screens_buttons.create_buttons(SAYINGS, 405, 200, 150, 35, WHITE, GOLD, SAYINGS)
            self.screens_buttons.create_buttons(JOKES, 405, 300, 150, 35, WHITE, GOLD, JOKES)

        elif self.state_02:
            if self.type_img == 1:
                
                img = pg.image.load('rsc/Consejos/Consejo'+str(num)+'.png')
                self.screen.blit(img,(285,45))
            elif self.type_img == 2:
                
                img = pg.image.load('rsc/Dichos/Dicho'+str(num)+'.png')
                self.screen.blit(img,(285,45))
            else:
                
                img = pg.image.load('rsc/Chistes/Chiste'+str(num)+'.png')
                self.screen.blit(img,(285,45))

            #Text
            self.myfont1 = pg.font.SysFont("monospace", 25)
            self.label_title = self.myfont1.render(f'Vuelto: ${self.money-self.price}', 1, BLACK)
            self.screen.blit(self.label_title, (550, 330))

            #Button
            self.screens_buttons.create_buttons("Cerrar", 205, 315, 130, 35, WHITE, GOLD, SHUTDOWN)
            


        elif self.state_03:
            #Text
            self.myfont1 = pg.font.SysFont("monospace", 45)
            self.label_title = self.myfont1.render("Password", 1, BLACK)
            self.screen.blit(self.label_title, (385, 135))
            #input text
            pg.draw.rect(self.screen,LIGHTBROWN,(375,185,235,25))
            self.input_text.keys(events)
            self.input_text.message(self.screen,376,185)
            #validation password
            if self.input_text.characters[0] == PASSWORD:
                self.screens_manage.screen_03 = False
                self.screens_manage.screen_04 = True
                self.input_text.characters = ['']
            #Button
            self.screens_buttons.create_buttons(BACK, 205, 315, 100, 35, WHITE, GOLD, BACK)


        elif self.state_04:
            #Text
            self.myfont1 = pg.font.SysFont("monospace", 35)
            self.label_title = self.myfont1.render("Modo Administracion", 1, BLACK)
            self.screen.blit(self.label_title, (300, 50))
            #Buttons
            self.screens_buttons.create_buttons(RESET, 405, 100, 150, 35, WHITE, GOLD, None)
            self.screens_buttons.create_buttons(SHUTDOWN, 405, 200, 150, 35, WHITE, GOLD, SHUTDOWN)
            self.screens_buttons.create_buttons(SALES_REPORT, 380, 300, 200, 35, WHITE, GOLD, None)
            self.screens_buttons.create_buttons(BACK, 205, 315, 100, 35, WHITE, GOLD, BACK)