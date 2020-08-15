import pygame as pg
from constants import *
import time 
import random
'''
Clase Button;
- Maneja los botones y actualiza estados
        Funciones:
        1) text_objects: retorna el texto renderisado en un rect
        E: text y el font
        S: una tupla con el texto renderizado y un rect

        2) create_buttons: Crea los botones y maneja sus acciones
        E: mensaje, posicion X y Y , ancho y alto, colores y la accion
        S: Dibuja los botones 

        3) archiveManage: maneja el archivo de mensajes y actualiza las ventas (NO FUNCIONA CORRECTAMENTE)
        E: codigo 

        4) update_screens: Actualiza el estado de las pantallas

        5) update_price: Actualiza el precio del producto

        6) update_money_entered: Actualiza el tipo de moneda que entro

        6) pay_action_update: Realiza la accion de pagar

'''

class Button:
    def __init__(self, screen):
        self.screen = screen
        self.smallText = pg.font.Font("freesansbold.ttf",20)

        self.screen_01 = False
        self.screen_02 = False
        self.screen_03 = False
        self.screen_04 = False
        self.breakloop = False

        self.price_option = 0
        self.money_entered = 0

        self.pay_action = 0
        self.random = 0
        

    def text_objects(self,text,font):
        self.text = text
        self.font = font
        self.textSurface = self.font.render(self.text,True,BLACK)
        return self.textSurface, self.textSurface.get_rect()

    def create_buttons(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        self.smallText = pg.font.Font("freesansbold.ttf",20)

        if x+w > mouse[0] > x and y+h> mouse[1] >y:
            pg.draw.rect(self.screen,ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "config":
                    self.screen_01 = False
                    self.screen_03 = True
                elif action == BACK:
                    self.screen_02 = False
                    self.screen_03 = False
                    self.screen_01 = True
                elif action == SHUTDOWN:
                    self.breakloop = True
                elif action == TIPS:
                    self.price_option = 1
                elif action == SAYINGS:
                    self.price_option = 2
                elif action == JOKES:
                    self.price_option = 3
                elif action == COIN1:
                    self.money_entered = 1
                    time.sleep(0.09)
                elif action == COIN2:
                    self.money_entered = 2
                    time.sleep(0.09)
                elif action == COIN3:
                    self.money_entered = 3
                    time.sleep(0.09)
                elif action == 20:
                    self.pay_action = 1
                    self.random = random.randint(1,15)
                    codigo = self.random
                elif action == 25:
                    self.pay_action = 2
                    self.random = random.randint(1,15)
                    codigo = self.random+15
                elif action == 30:
                    self.pay_action = 3
                    self.random = random.randint(1,20)
                    codigo = self.random+30

      
        else:
            pg.draw.rect(self.screen,ic,(x,y,w,h))
        
        self.textSurf,self.textRect = self.text_objects(msg,self.smallText)
        self.textRect.center = ( (x+(w/2)) , (y+(h/2)) )
        self.screen.blit(self.textSurf,self.textRect)

    #maneja archivos (no completa la suma de las ventas)
    def archiveManage(self,codigo):
        archive = open('mensajes.txt','r+')
        for line in archive:
            countSlash = 0
            code = ''
            count = 0
            wait = 0
            num = ''
            for i in line:
                count +=1
                if wait ==1:
                    num +=i
                if i == '/':
                    countSlash +=1
                if countSlash == 1:
                    code += i 
                if int(code) == codigo:
                    if countSlash == 3 :
                        wait =1
            if num != '':
                cambio = int(num)+1
                for i in line:
                    count +=1
                    if wait2 ==1:
                        num +=i
                    if i == '/':
                        countSlash +=1
                    if countSlash == 1:
                        code += i 
                    if int(code) == codigo:
                        if countSlash == 3 :
                            wait2 =1
                        

    def update_screens(self):
        if self.breakloop:
            return 0
        if self.screen_01:
            return 1
        elif self.screen_02:
            return 2
        elif self.screen_03:
            return 3
        elif self.screen_04:
            return 4

    def update_price(self):
        if self.price_option == 1:
            return 1
        elif self.price_option == 2:
            return 2
        elif self.price_option == 3:
            return 3

    def update_money_entered(self):
        if self.money_entered == 1:
            self.money_entered =0
            return 1
        elif self.money_entered == 2:
            self.money_entered =0
            return 2
        elif self.money_entered == 3:
            self.money_entered =0
            return 3

    def pay_action_update(self):
        if self.pay_action == 1:
            return [self.pay_action,self.random]
        elif self.pay_action == 2:
            return [self.pay_action,self.random]
        elif self.pay_action == 3:
            return [self.pay_action,self.random]
        return 0

