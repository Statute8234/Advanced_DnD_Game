from ursina import *

# PauseMenu
class PauseMenu(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)

        self.pause_menu = Entity(parent=self,enabled = True)
        self.player = None
        self.main_menu = None
        mouse.locked = False

        def play():
            mouse.position = (0, 0, 0)
            mouse.locked = True
            self.pause_menu.disable()

        resume_button = Button(text="Resume", color=color.black, scale_y=0.1, scale_x=0.3, y=0.12,parent=self.pause_menu)
        resume_button.on_click = Func(play)
        quit_button = Button(text="Quit", color=color.black, scale_y=0.1, scale_x=0.3, y=-0.1,parent=self.pause_menu)
        quit_button.on_click = application.quit
