from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class but(GridLayout):
    def __init__(self,**kwargs):
        super(but, self).__init__(**kwargs)
        self.cols = 1

        self.firstgread = GridLayout()
        self.firstgread.cols = 2

        self.firstgread.add_widget(Label(text = 'name: '))
        self.name = TextInput(multiline= False)
        self.firstgread.add_widget(self.name)

        self.firstgread.add_widget(Label(text='pizza: '))
        self.pizza = TextInput(multiline=False)
        self.firstgread.add_widget(self.pizza)

        self.firstgread.add_widget(Label(text='color: '))
        self.color = TextInput(multiline=False)
        self.firstgread.add_widget(self.color)

        self.add_widget(self.firstgread)


        self.ba = Button(text='submit',font_size = 30,size_hint_y=None,height=50)
        self.ba.bind(on_press=self.pre)
        self.add_widget(self.ba)

    def pre(self,instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'{name}   \n{pizza}\n{color}')

        self.add_widget(Label(text = f'{name}\n{pizza}\n{color}',size_hint_y=.05,size_hint_x=None))

        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class myapp(App):
    def build(self):
        return but()


if __name__ == '__main__':
    myapp().run()
