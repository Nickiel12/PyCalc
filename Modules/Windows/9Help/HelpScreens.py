
from pathlib import Path
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder

ComboHlpPath = Path("Configs/Helptexts/Combo_Help.cfg")
StatHlpPath = Path("Configs/Helptexts/Stat_Help.cfg")
PermHlpPath = Path("Configs/Helptexts/Perm_Help.cfg")


#all this is the screen that is parented to the master files
class HelpScreens(Screen):

    def build(self, *args):
        print("built")

class HelpManager(ScreenManager):
    pass

class HelpMain(Screen):
    pass

class HelpComboScreen(Screen):
    
    with open(ComboHlpPath, "r") as configfile:
        combo_str = str(configfile.read())

    def build_menu(self, *args):
        print ("changed the menu")
        

class HelpStatScreen(Screen):

    with open(StatHlpPath, "r") as configfile:
        stat_str = str(configfile.read())

    def build_menu(self, *args):
        print("changed the menu")

class HelpPermScreen(Screen):

    with open(PermHlpPath, "r") as configfile:
        perm_str = str(configfile.read())

    def build_menu(self, *args):
        print("changed the menu")
