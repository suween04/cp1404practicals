from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class YourApp(App):
    def build(self):
        return Builder.load_file('box_layout.kv')

    def handle_greet(self):
        # Get the name from the TextInput and display greeting
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        # Reset the text input and label when Clear is clicked
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    YourApp().run()
