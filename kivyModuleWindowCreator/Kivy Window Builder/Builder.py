from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import tkinter as Tkinter
from tkinter import filedialog
from string import Template

import sys
import os
from pathlib import PurePath

class Window(FloatLayout):
    def browse(self):
        Tkinter.Tk().withdraw() # Close the root window
        in_path = filedialog.askdirectory()
        self.ids.PathInput.text = in_path

    def build_windows_template(self):
        name = self.ids.NameInput.text
        if name == '':
            self.popup_emptyfield('Name')
            return
        name = name.replace(' ', '_')

        path = self.ids.PathInput.text
        print(path)
        if path == '':
            self.popup_emptyfield('Build Directory')
            return
        try:
            os_path = PurePath(path)
            folder_path = os_path / name
            if folder_path == '.':
                self.popup_emptyfield('Build Directory')
                return
        except ValueError:
            self.popup_errorfield('Build Directory')
            return
        try:
            os.mkdir(folder_path)
            self.write_kv_file(folder_path, name)
            self.write_py_file(folder_path, name)
            self.success()
        except FileExistsError:
            self.popup_folder_exist()
            return
    
    def write_kv_file(self, dir_path, module_name):
        file_path = str(str(dir_path / (module_name[1::])) + '.kv')
        module_name = module_name[1::]

        with open('kvTemplate.txt', 'r') as kv_template:
            kv_template_str = kv_template.read()
            kv_content = Template(kv_template_str).substitute(module_nameScreens=str(module_name) + 'Screens', 
                module_nameManager = str(module_name) + 'Manager',
                module_nameMainScreen = str(module_name) + 'MainScreen')
            with open(file_path, 'w+') as file:
                file.write(kv_content)
    
    def write_py_file(self, dir_path, module_name):
        file_path = str(str(dir_path / (module_name[1::])) + 'Screens.py')
        class_names = module_name[1::]
        with open('pyTemplate.txt', 'r') as py_template:
            py_template_str = py_template.read()
            py_content = Template(py_template_str).substitute(module_nameScreens=str(class_names) + 'Screens', 
                module_nameManager = str(class_names) + 'Manager',
                module_nameMainScreen = str(class_names) + 'MainScreen')
            with open(file_path, 'w+') as file:
                file.write(py_content)
    
    def popup_emptyfield(self, errored_input):
        error_popup = Popup(title='Required Field Left Blank',
            content=Label(text=str(str(errored_input)+' is a required field, and was left blank')),
            size_hint=(.5, .5))
        error_popup.open()

    def popup_errorfield(self, errored_input):
        error_popup = Popup(title='Required Field Left Blank',
            content=Label(text=str('The input in the '+str(errored_input)+' is incorrect')),
            size_hint=(.5, .5))
        error_popup.open()
    
    def popup_folder_exist(self, ):
        error_popup = Popup(title='Folder Exist',
            content=Label(text='That folder already exists'),
            size_hint=(.5, .5))
        error_popup.open()
    
    def success(self):
        popup = Popup(title='Closing',
            content=Label(text=str('Success')),
            size_hint=(.5, .5),
            on_dismiss = self.close)
        popup.open()

    def close(self, *args, **kwargs):
        sys.exit(0)

class BuilderApp(App):
    def build(self):
        return Window()

if __name__ == "__main__":
    BuilderApp().run()
