from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):
        names = ['Alice', 'Bob', 'Charlie', 'David']
        for name in names:
            label = Label(text=name)
            self.root.ids.labels_box.add_widget(label)

if __name__ == '__main__':
    DynamicLabelsApp().run()
