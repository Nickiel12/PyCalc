import importlib
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

if __name__ == '__main__':
    import Combination
else:
    PACKAGE = r'Modules.Windows.3Combination.Combination'
    COMBO = importlib.import_module(PACKAGE)
Combination = COMBO.Combination

class CombinationScreens(Screen):

    pass

class ComboMain(ScreenManager):

    pass

class ComboCalcScreen(Screen):

    def add_input(self):
        input_num = self.ids.ComboTextInput.text
        spots_num = self.ids.ComboSpotsInput.text

        try: 
            input_num = int(input_num)
        except ValueError:
            self.throw_value_error('Top Input')

        try:
            spots_num = int(spots_num)
            combo_output = Combination(input_num, spots_num)
        except ValueError:
            combo_output = Combination(input_num)
            
        if isinstance(spots_num, int):
            output_num = str(str(input_num) +'/'+ str(spots_num) + ' spots: ' + combo_output)
            font_size = 60
        else:
            font_size = 70
            output_num = str(str(input_num) + ': ' + combo_output)
        label_text = self.add_newlines(output_num)

        output_label = ScaleLabel(text=label_text, size_hint= [0.8, .5],
             pos_hint={'right':0.91, 'top':.79}, font_size=font_size)

        layout_wrapper = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        layout_wrapper.add_widget(output_label)
        self.ids.ComboOutputGrid.add_widget(layout_wrapper)

    def add_newlines(self, input_string, max_line_length = 30):
        character_list = []
        iter_num = 0
        for c in input_string:
            character_list.append(c)

        while iter_num < len(character_list)-1:
            if iter_num % max_line_length == 0 and iter_num != 0:
                character_list.insert(iter_num+1, '-\n')
            iter_num += 1

        output_str = ''.join(character_list)
        return output_str

    def clear(self):
        self.ids.ComboTextInput.text = ''
        self.ids.ComboSpotsInput.text = 'Spots/Places'
        self.ids.ComboOutputGrid.clear_widgets()

    def throw_value_error(self, label_in_question):
        pass

class ScaleLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)