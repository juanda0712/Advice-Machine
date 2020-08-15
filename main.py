import pygame as pg
from constants import *
from screensManager import *
from buttonsManager import *

'''
Clase Main;
- Maneja las operaciones mas importantes del programa
        Funciones:
        1) button_call: Crea los botones de "config" y de las monedas y les asigna un a funcion a cada uno 
        S: 4 botones, cada uno con una funcion diferente 

        2) update_screens: Es la funcion que actualiza las pantallas y cambia entre ellas 
        S: El estado de pantalla (en que pantalla se esta en cada momento)

        3) update_price: Constantemente actuaiza el precio del producto que se desea comprar
        E: La orden de los botones para elegir el producto que se desea comprar
        S: Precio del producto que se desea comprar

        4) text_price: Coloca el precio del producto que se desea comprar asi como el dinero que el cliente mete
        E: El producto a comprar
        S: El precio del producto y cuando dinero ha puesto el cliente

        5) update_money_entered: Actualiza constantemente la cantidad de dinero que el usuario ingreso 

        6) pay_action_update: Realiza la accion del pago
        E: Precio del producto y el dinero que se ingreso en la maquina

        6) main: Ejecuta en un bucle las funciones

''' 

pg.init()
class Main:
    def __init__(self):
        #self.image = pg.image.load('rsc/Consejo01.png')
        self.breakloop = False
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption('Advice Machine')
        self.clock = pg.time.Clock()
        self.screen_img = pg.image.load('rsc/pantalla.png')
        self.moneda5 = pg.image.load('rsc/moneda5.png')
        self.moneda10 = pg.image.load('rsc/moneda10.png')
        self.moneda15 = pg.image.load('rsc/moneda15.png')

        self.screen_01 = True
        self.screen_02 = False
        self.screen_03 = False
        self.screen_04 = False

        self.input_screens = Screens(self.screen)
        self.screens_buttons = Button(self.screen)
        
        self.price = 0
        self.money = 0

        self.type_img = 0
        self.num = 0

    def button_call(self):
        self.screens_buttons.create_buttons(CONFIG, 10, 40, 140, 35, WHITE, GOLD, "config")
        self.screens_buttons.create_buttons(PAY, 450, 595, 80, 50, WHITE, GOLD, self.price) 
        self.screens_buttons.create_buttons(COIN1, 30, 560, 70, 70, GRAY, GRAY, COIN1)
        self.screens_buttons.create_buttons(COIN2, 145, 560, 70, 70, GRAY, GRAY, COIN2)
        self.screens_buttons.create_buttons(COIN3, 255, 560, 70, 70, GRAY, GRAY, COIN3)

    def update_screens(self):
        update = self.screens_buttons.update_screens()
        if update == 0:
            self.breakloop = True
        if update == 1:
            self.screen_01 = True
            self.screen_03 = False
            self.screen_04 = False
        elif update ==2:
            self.screen_01 = False
            self.screen_02 = True
        elif update ==3:
            self.screen_01 = False
            self.screen_03 = True 
        elif update ==4:
            self.screen_03 = False
            self.screen_04 = True
        
    def update_price(self):
        action = self.screens_buttons.update_price()
        if action ==1: #tips
            self.price = 20
        elif action ==2: #sayings
            self.price = 25
        elif action ==3: #jokes
            self.price = 30

    def text_price(self):
        #amount payable
        self.myfont1 = pg.font.SysFont("monospace", 25)
        self.label_title = self.myfont1.render(f'Precio: ${self.price}', 1, BLACK)
        self.screen.blit(self.label_title, (560, 535))
        #amount of money entered
        self.myfont2 = pg.font.SysFont("monospace", 34)
        self.label_title = self.myfont2.render(f'${self.money}', 1, BLACK)
        self.screen.blit(self.label_title, (615, 595))

    def update_money_entered(self):
        action = self.screens_buttons.update_money_entered()
        if action ==1: #$5
            self.money += 5
        elif action ==2: #$10
            self.money += 10
        elif action ==3: #$15
            self.money += 15

    def pay_action_update(self,price,money):
        
        action = self.screens_buttons.pay_action_update()
        if action != 0:
            if action[0] == 1 and money >= 20:
                
                self.num = action[1]
                if money >= 20 and price >=20: 
                    if money >= price:
                        self.screen_01 = False
                        self.screen_02 = True
                        self.type_img = 1
            elif action[0] == 2 and money >= 25:
                self.num = action[1]
                if money >= 25 and price >=25:
                    if money >= price:
                        self.screen_01 = False
                        self.screen_02 = True
                        self.type_img = 2
            elif action[0] == 3 and money >= 30:
                self.num = action[1]
                if money >= 30 and price >=30:               
                    if money >= price:
                        self.screen_01 = False
                        self.screen_02 = True
                        self.type_img = 3

    def main(self):
        while not self.breakloop:

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.breakloop = True

            self.screen.fill(GRAY)
            self.screen.blit(self.screen_img,(160,0))
            pg.draw.rect(self.screen,YELLOW,(540,575,200,80))

            self.update_screens() 
            self.update_price()   
            self.text_price() 
            self.update_money_entered()
            self.pay_action_update(self.price,self.money)    
            self.button_call()    
            self.screen.blit(self.moneda5,(30, 560))
            self.screen.blit(self.moneda10,(145, 560))
            self.screen.blit(self.moneda10,(255, 560))

            self.input_screens.__draw__(self.screen_01, self.screen_02,
             self.screen_03, self.screen_04,events, self.screens_buttons, 
             self.screens_buttons,self.type_img,self.num,self.price,self.money)

            pg.display.update()
            self.clock.tick(30)


exe = Main()
exe.main()
pg.quit()

