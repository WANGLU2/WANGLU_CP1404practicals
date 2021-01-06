"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 06/01/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window




class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = float(self.root.ids.input_number.text)
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
