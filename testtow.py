from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class win(Widget):

    name = ObjectProperty()
    pizza = ObjectProperty()
    color = ObjectProperty()
    def opr(self):
        name  = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'{name}{pizza}{color}')

        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''

class mysecondapp(App):
    def build(self):
        return win()

if __name__ == '__main__':
    mysecondapp().run()