from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from Modules.Windows.ReadModules import ReadModules as ReadM

from kivy.core.window import Window
Window.clearcolor = (.1, .1, .13, 1)


class Controller(ScreenManager):
    pass


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.ReadMods, 0)

    def ReadMods(self, *args):
        RM = ReadM()
        RM.read_modules(passed_ob=self)

    def build_help(self, *args):
        print("changed the menu")


class PycalcApp(App):
    def build(self):
        #uncomment to use the custom icon in the file listed below
        #path = PurePath('Resources\\PyCalcIcoPng.png')
        #self.icon = str(path)
        return Controller()

if __name__ == '__main__':
    PycalcApp().run()
