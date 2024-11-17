from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class MilesToKmApp(App):
    def build(self):
        return Builder.load_file('convert_miles_km.kv')

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles_input.text)
            self.root.ids.miles_input.text = str(miles + value)
        except ValueError:
            self.root.ids.miles_input.text = '0'

    def handle_convert(self):
        try:
            miles = float(self.root.ids.miles_input.text)
            km = miles * 1.60934  # Conversion constant
            self.root.ids.km_label.text = f"{km:.2f} km"
        except ValueError:
            self.root.ids.km_label.text = "0.0 km"

if __name__ == '__main__':
    MilesToKmApp().run()
