import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def btn(self):
        show_popup()

class WindowManager(ScreenManager):
    pass


class Pop(FloatLayout):
    pass

kv = Builder.load_file("my.kv")




class MyMainApp(App):
    def build(self):
        return kv


def show_popup():
    show = Pop()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()


if __name__ == '__main__':
    MyMainApp().run()
