from examples.game.game import RendererApp
from kivy.resources import resource_add_path

if __name__ == "__main__":
    resource_add_path("assets")
    resource_add_path("assets/assets")
    RendererApp().run()