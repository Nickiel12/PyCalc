import importlib

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    import Statistic_Calculator as StatCalc
else:
    package = r'Modules.Windows.1Statistic_Calculator.Statistic_Calculator'
    Statistic_Calculator = importlib.import_module(package)
    StatCalc = Statistic_Calculator


class Statistic_CalculatorScreens(Screen):
    pass

class StatisticManager(ScreenManager):
    pass

class StatisticScreen(Screen):
    input_list = []
    prev_input_label_list = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.on_startup, 0)

    def on_startup(self, *args):
        self.ids.CountManager.current = 'BlankScreen'

    def focus_set(self, *args):
        self.ids.DigitInput.focus = True
    
    def add_input(self):
        num_input = self.ids.DigitInput.text
        self.ids.DigitInput.text = ''
        Clock.schedule_once(self.focus_set, 0.2)
        try: 
            num_input = float(num_input)
        except ValueError:
            self.popup_error_inputfield()
            return
        try: 
            self.input_list.append(num_input)
            label_text = (str(num_input))
            output_label = ScaleLabel(text=label_text, size_hint= [0.8, .5], pos_hint={'right':0.91, 'top':.79}, font_size=50)

            layout_wrapper = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
            layout_wrapper.add_widget(output_label)
            self.prev_input_label_list = layout_wrapper
            self.ids.InputGrid.add_widget(layout_wrapper)
        except ValueError:
            print('Throwing down the gauntlet!!!!>_< (an error needs to be inserted)')

    def popup_error_inputfield(self, ):
        error_popup = Popup(title='Error',
            content=Label(text='Input field has no input,\nor it has an invalid input', font_size=20),
            size_hint=(.5, .5))
        error_popup.open()
    
    def popup_error(self, error):
        error_popup = Popup(title='Error',
            content=Label(text=str(error), font_size=20),
            size_hint=(.5, .5))
        error_popup.open()

    def remove_most_prev_input(self):
        try:
            self.input_list[-1] = None
            self.ids.InputGrid.remove_widget(self.prev_input_label_list)
        except IndexError:
            self.popup_error('There are no items to remove')

    def calculate(self):
        if len(self.input_list) <= 1:
            self.popup_error('There are no inputs')
            return
        average = StatCalc.average(self.input_list)
        count_dict = StatCalc.count_two(self.input_list)
        median = StatCalc.median(self.input_list)
        standard_deviation = StatCalc.standard_deviation(self.input_list)
        self.ids.InputGrid.clear_widgets()
        self.input_list.clear()

        self.output_answers(average, count_dict, median, standard_deviation)

    def output_answers(self, average, count_dict, median, standard_deviation,):
        global CountScreenInstance
        CountScreenInstance.ids.ChartBox.clear_widgets()
    
        self.ids.AverageLabel.text = str(average)
        self.ids.MedianLabel.text = str(median)
        self.ids.StandDeviate.text = str(standard_deviation)
        
        fig, ax = plt.subplots()
        count_names = list(count_dict.keys())
        y_pos = np.arange(len(count_names))
        count_values = list(count_dict.values())
        ax.barh(y_pos, count_values)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(count_names)
        ax.grid(True)
        canvas = fig.canvas

        CountScreenInstance.ids.ChartBox.add_widget(canvas)

    def clear_output(self):
        global CountScreenInstance
        CountScreenInstance.ids.ChartBox.clear_widgets()
        self.ids.AverageLabel.text = ""
        self.ids.MedianLabel.text = ""
        self.ids.StandDeviate.text = ""

            

class CountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.on_startup, 0)

    def on_startup(self, *args):
        global CountScreenInstance
        CountScreenInstance = self

    def explain_popup(self):
        content_label = Label(text = 'This Count window counts how many\n of each number there are in a list', font_size=20)
        popup = Popup(title='Count Explanation',
            content=content_label,
            size_hint=(.75, .75))
        popup.open()

class BlankScreen(Screen):
    pass

class ScaleLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
