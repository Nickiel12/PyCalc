from kivy.uix.screenmanager import Screen, ScreenManager
import importlib
from pathlib import Path
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

if __name__ == '__main__':
    import Permutation
else:
    package = r'Modules.Windows.2Permutation.Permutation'
    Permutation = importlib.import_module(package)
Permute = Permutation.Permute

class PermutationScreens(Screen):
    pass
    
class PermMain(ScreenManager):
    pass

class PermCalcScreen(Screen): #30 is the max character length that looks good
    def add_input(self):
        input_num = self.ids.PermTextInput.text
        spots_num = self.ids.PermSpotsInput.text
        try:
            spots_num = int(spots_num)
            permed_num = Permute(input_num, spots_num)
        except ValueError:
            permed_num = Permute(input_num)
        if isinstance(spots_num, int):
            output_num = str(input_num +'/'+ str(spots_num) + ' spots: ' + permed_num)
            font_size = 60
        else:
            font_size = 70
            output_num = str(input_num + ': ' + permed_num)
        label_text = self.add_newlines(output_num)
            
        output_label = ScaleLabel(text=label_text, size_hint= [0.8, .5], pos_hint={'right':0.91, 'top':.79}, font_size=font_size)

        layout_wrapper = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        layout_wrapper.add_widget(output_label)
        self.ids.PermOutputGrid.add_widget(layout_wrapper)
    
    def add_newlines(self, input_string, max_line_length = 30):
        Character_List = []
        iter_num = 0
        for c in input_string:
            Character_List.append(c)

        while iter_num < len(Character_List)-1:
            if iter_num % max_line_length == 0 and iter_num != 0:
                Character_List.insert(iter_num+1, '-\n')
            iter_num += 1

        output_str = ''.join(Character_List)
        return output_str

    def clear(self):
        self.ids.PermTextInput.text = ''
        self.ids.PermSpotsInput.text = ""
        self.ids.SpotsInput.text = 'Spots/Places'
        self.ids.OutputGrid.clear_widgets()


class ScaleLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)