from ursina import *

class MainMenu(Entity):
    def __init__(self, player):
        super().__init__(parent = camera.ui)

        self.main_menu = Entity(parent = self, enabled = True)
        self.player = player
        mouse.locked = False

        def Play():
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()

        story_button = Button(text = "Play", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.main_menu)
        quit_button = Button(text = "Quit", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button.on_click = application.quit
        story_button.on_click = Func(Play)
