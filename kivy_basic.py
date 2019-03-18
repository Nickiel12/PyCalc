import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib import pyplot
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

fig, ax = pyplot.subplots()
# A canvas must be manually attached to the figure (pyplot would automatically
# do it).  This is done by instantiating the canvas with the figure as
# argument.
canvas = fig.canvas
ax.plot([1, 2, 3])
ax.set_title('exponential energy usage')
ax.grid(True)
ax.set_xlabel('time')
ax.set_ylabel('volts')
print(type(canvas))

class kivy_basicApp(App):
    def build(self, **kwargs):
        super().__init__(**kwargs)
        boxlay = BoxLayout()
        boxlay.add_widget(canvas)
        return(boxlay)

if __name__ == "__main__":
    kivy_basicApp().run()