from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class inventory(GridLayout):

    def __init__(self, **kwargs):
        super(inventory, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Name'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text='Surname'))
        self.surname = TextInput(multiline=False)
        self.add_widget(self.surname)
        self.add_widget(Label(text='Print password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return inventory()


if __name__ == '__main__':
    MyApp().run()