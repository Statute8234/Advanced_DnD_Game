from ursina import *
from ursina.shaders import lit_with_shadows_shader

# sword
class Sword(Entity):
    def __init__(self,position=(0, 0, 0)):
        super().__init__()
        self.parent = camera.ui
        self.position = position
        self.model = 'weapons/13032_Claymore_Sword_v1_l3.obj'
        self.scale = 0.009
        self.y = 0.5
        self.x = 0.5
        self.rotation_z = 90
        self.rotation_x = 90
        self.rotation_y = 180
        self.shader = lit_with_shadows_shader

    def update(self):
        if held_keys['gamepad right trigger']:
            self.animate_rotation((50,100,180),duration = 0.5)
            self.animate_position((0.2,0.5,0),duration = 0.5)
            self.animate_rotation((90, 90, 180), delay = 1, duration=0.5)
            self.animate_position((0.5, 0.5, 0), delay = 1,duration=0.5)

# shield
class Shield(Entity):
    def __init__(self,position=(0, 0, 0)):
        super().__init__()
        self.parent = camera.ui
        self.position = position
        self.model = 'weapons/11502_Shield_v202.obj'
        self.y = -0.8
        self.x = -0.4
        self.rotation_x = -90
        self.scale = 0.01
        self.shader = lit_with_shadows_shader

    def update(self):
        if held_keys['gamepad left trigger']:
            self.animate_position((-0.2, -0.3, 0), duration=0.5)
            self.animate_position((-0.4, -0.8, 0), duration=0.5,delay = 1)
