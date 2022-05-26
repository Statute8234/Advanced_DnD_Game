import random
from ursina import *
from ursina.shaders import lit_with_shadows_shader

class Item(Button):
    def __init__(self,position=(0, 0, 0)):
        super().__init__()
        self.parent = scene
        self.position = position
        RM = random.randint(0,2)
        if RM == 0:
            self.model = 'weapons/11502_Shield_v202.obj'
            self.y = 0.5
            self.scale = 0.01
            self.color = color.random_color()

            self.name = 'Shield'
            self.attack,self.amount = -1,-1
            self.armor, self.weight, self.cost = random.randint(0, 20), round(random.uniform(0, 9), 1), round(random.uniform(0, 99), 2)
            self.tooltip = Tooltip(text='Shield: \narmor: {} \nweight: {} \ncost: ${:.2f}'.format(self.armor, self.weight, self.cost))
        if RM == 1:
            self.model = 'weapons/13032_Claymore_Sword_v1_l3.obj'
            self.y = 0.1
            self.scale = 0.01
            self.color = color.random_color()

            self.name = 'Sword'
            self.amount = -1
            self.attack, self.weight, self.cost = random.randint(0, 20), round(random.uniform(0, 9), 1), round(random.uniform(0, 99), 2)
            self.tooltip = Tooltip(text='Sword: \nattack: {} \nweight: {} \ncost: ${:.2f}'.format(self.attack, self.weight, self.cost))
        if RM == 2:
            self.model = 'cube'
            self.texture = 'potions/potion.png'
            self.scale_y = 0.01
            self.y = 0.1
            self.color = color.white

            self.name = 'Health Potion'
            self.attack,self.weight = -1,-1
            self.cost,self.amount = round(random.uniform(0, 99), 2),random.randint(0, 100)
            self.tooltip = Tooltip(text= 'Health Potion \namount: {} \ncost: ${:.2f}'.format(self.amount,self.cost))

        self.shader = lit_with_shadows_shader
        self.collider = 'mesh'

    def input(self, key):
        if self.hovered:
            if held_keys['gamepad y']:
                print(self.name,self.attack,self.amount,self.weight,self.cost)
                destroy(self)
