import random

import ursina
from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar

# hand made files
from player import Gamepadcontroller
from mainmenu import MainMenu
from hand import Sword, Shield,inventory
from pickItems import Chest
from playerStorige import Player_Inventory

ursina.SmoothFollow = True
gamepad = ['gamepad dpad left', 'shift', 'gamepad dpad right', 'gamepad dpad down', 'gamepad dpad up', 'gamepad x', 'gamepad a', 'gamepad b', 'gamepad y', 'gamepad left shoulder', 'gamepad right shoulder', 'gamepad back', 'gamepad start', 'gamepad left stick', 'gamepad right stick', 'gamepad left stick x', 'gamepad left stick y', 'gamepad right stick x', 'gamepad right stick y', 'gamepad left trigger', 'gamepad right trigger']

PauseMenu_opened = 0
def update():
    global player_hp,PauseMenu_opened
    # PauseMenu
    if held_keys['gamepad start']:
        PauseMenu_opened += 1
        if PauseMenu_opened % 2:
            try:
                MainMenu.disable(self = player)
            except ValueError:
                pass
        else:
            player.disable()
            MainMenu(player)
    # inventory
    if held_keys['gamepad back']:
        PauseMenu_opened += 1
        if PauseMenu_opened % 2:
            try:
                Player_Inventory.disable(self = player)
            except ValueError:
                pass
        else:
            player.disable()
            Player_Inventory(player,inventory)
    # if hp is above 100
    if player_hp.value > 100:
        player_hp = 100
    # respond
    if player_hp.value <= 0:
        player_hp.value = 100
        player.position = (0, 1, 0)
    # if the player falls off the map
    if player.y <= -1:
        player_hp.value -= 1
    # heal player
    if held_keys['gamepad right shoulder']:
        if player_hp.value < 100:
            for value in inventory:
                if value[0] == 'Health Potion':
                    player_hp.value += value[1]
                    inventory.remove(value)
                    print_on_screen(text='-1 health potion', position=(0, 0))
        else:
            check = 0
            for value in inventory:
                if value[0] == 'Health Potion':
                    check = 1
            if check == 1:
                print_on_screen(text = 'your health is at 100',position = (0,0))
            else:
                print_on_screen(text='you do not have any health potions', position=(0, 0))

app = Ursina()
# player
player = Gamepadcontroller(speed = 10)
player_hp = HealthBar(parent = camera.ui,bar_color = color.red)
# player_hand
shield = Shield()
sword = Sword()
# chest
for i in range(10):
    chest = Chest(position = (random.randint(-30,30),0,random.randint(-33,25)))
# ground
ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4),shader = lit_with_shadows_shader)
# sky
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()
app.run()
