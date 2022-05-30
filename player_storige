from ursina import *
from ursina.shaders import lit_with_shadows_shader

from hand import Sword, Shield,inventory
from pick_up_items import inventory

# inventory
class Player_Inventory(Entity):
    def __init__(self,player,inventory):
        super().__init__(parent=camera.ui)

        self.player_inventory = Entity(parent=self, enabled=True)
        self.player = player
        mouse.locked = False

        def Equip():
            print('test')

        icon = Button(text="Test", color=colors.blue, scale_y=0.1, scale_x=0.3, y=0.02, parent=self.player_inventory,collider='box')
        for value in inventory:
            Button(parent = icon,text = value[0])
        icon.add_script(Scrollable())

        def Exit():
            self.player.enable()
            mouse.locked = True
            self.player_inventory.disable()
            self.player_inventory.disable()
            self.player_inventory.disable()


        quit_button = Button(text="Exit", color=color.black, scale_y=0.1, scale_x=0.3, y=-0.22, x = 0.3,parent=self.player_inventory)
        icon.on_click = Func(Equip)
        quit_button.on_click = Func(Exit)
