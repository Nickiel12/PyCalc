from pathlib import Path
import os
import importlib
from functools import partial

from kivy.uix.button import Button
from kivy.lang.builder import Builder

class ReadModules():
    def read_modules(self, passed_ob):
        path = Path("Modules/Windows")
        files = os.listdir(path)
        print(files)
        modules = []
                
        for current_file in files:
            if not current_file[-3] == '.':
                if not current_file == 'GuideLines.txt':
                    if not current_file =="__pycache__":
                        file_name = current_file[1:]
                        button_text = file_name.replace('_', ' ')
                        modules.append(str(file_name))

                        modulename = file_name + "Screens"
                        KVFile = str("Modules/Windows/{}/{}.kv").format(current_file, file_name)

                        package = str("Modules.Windows.{}.{}").format(current_file, modulename)
                        my_module = importlib.import_module(package)
                        Builder.load_file(KVFile)

                        EntryClass = getattr(my_module, modulename)
                        LoadScreen = EntryClass(name = modulename)
                        passed_ob.parent.add_widget(LoadScreen)
                        button = Button(text = button_text)
                        button.bind(on_press = partial(self.SwitchScreen, passed_ob, modulename))

                        passed_ob.ids.ButtonGrid.add_widget(button)
        print('Current Modules Loaded:')
        print(modules)

    def SwitchScreen(self, rootScreen, EntryScreen, *args):
        rootScreen.manager.current = EntryScreen