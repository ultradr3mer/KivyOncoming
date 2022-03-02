from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.uix.widget import Widget
from kivy.resources import resource_find
# the findow Import is nessesarry, otherwise the app does not start
from kivy.core.window import Window
from kivy.graphics.transformation import Matrix
from kivy.graphics.opengl import glEnable, glDisable, GL_DEPTH_TEST
from kivy.graphics import RenderContext, Callback, Color
from examples.game.obj_loader import Obj

class Renderer(Widget):
    def __init__(self, **kwargs):
        self.canvas = RenderContext(compute_normal_mat=False)
        self.canvas.shader.source = resource_find('shader.glsl')
        self.scene = Obj(resource_find("tesla.obj"))
        super(Renderer, self).__init__(**kwargs)
        with self.canvas:
            self.cb = Callback(self.setup_gl_context)
            self.setup_scene()
            self.cb = Callback(self.reset_gl_context)
        Clock.schedule_interval(self.update_glsl, 1 / 60.)

    def update_glsl(self, delta):
        asp = self.width / float(self.height)
        proj = Matrix().view_clip(-asp * 10, asp * 10, -10, 10, 0, 1, 0)
        self.canvas['projection_matrix'] = proj
        self.canvas['modelview_matrix'] = Matrix().identity()

    def setup_gl_context(self, *args):
        glEnable(GL_DEPTH_TEST)

    def reset_gl_context(self, *args):
        glDisable(GL_DEPTH_TEST)

    def setup_scene(self):
        Color(0, 0, 0, 0)
        self.mesh = self.scene.make_mesh()
        self.mesh.texture = Image(resource_find("tesla.dds")).texture


class RendererApp(App):
    def build(self):
        return Renderer()


if __name__ == "__main__":
    RendererApp().run()
