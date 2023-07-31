from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import subprocess

class MyApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        btn = Button(text="Start Mitmproxy")
        btn.bind(on_press=self.callback)
        layout.add_widget(btn)
        return layout

    def callback(self, instance):
        subprocess.call(['python3', 'my_mitmproxy.py'])

if __name__ == '__main__':
    MyApp().run()

