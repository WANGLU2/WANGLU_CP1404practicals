from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        print("handle calculate")

        miles = self.convert_to_number(text)
        result = miles * 1.60934 # 1 miles = 1.60934 Kilometres
        self.output_km = str(result)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)



    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0


MilesConverterApp().run()