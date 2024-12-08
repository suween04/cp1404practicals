from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class SquareApp(App):
    def build(self):
        return Builder.load_file('squaring.kv')

    def handle_calculate(self, number_text):
        try:
            number = float(number_text)
            self.root.ids.output_label.text = str(number ** 2)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

if __name__ == '__main__':
    SquareApp().run()
