from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class gri(Widget):

    name=ObjectProperty()
    pizza=ObjectProperty()
    color=ObjectProperty()


    def pre(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'{name}{pizza}{color}')

        self.name.text =''
        self.pizza.text = ''
        self.color.text = ''







class myapp(App):
    def build(self):
        return gri()

if __name__ == '__main__':
    myapp().run()