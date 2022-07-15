from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder

Builder.load_file('threeapp.kv')

class wid(Widget):
    pass


    '''
    name = ObjectProperty()
    def opr(self):
        name = self.name.text
        print(f'{name}')
        self.name.text = ''
'''

class threeapp(App):
    def build(self):
        return wid()

if __name__ == "__main__":
    threeapp().run()