import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
import predict_msh
from PIL import Image as ImagePil
import threading



class MainWindow(Screen):
    pass


class SecondWindow(Screen):

    def btn(self, *args):
        pbar = ProgressBar(value=25, max=100)
        popup = Popup(content=pbar, title='Calculating...')
        popup.open()
        threading.Thread(target=select_to(*args)).start()
        popup.dismiss()


class ThirdWindow(Screen):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png('./source/image_pred.jpg')

    def btn(self):
        pbar = ProgressBar(value=25, max=100)
        popup = Popup(content=pbar, title='Calculating...')
        popup.open()
        threading.Thread(target=select_to(['./source/image_pred.jpg'])).start()
        popup.dismiss()


class WindowManager(ScreenManager):
    pass


class Pop(FloatLayout):
    pass


def select_to(*args):
    try:
        prediction, danger, info = predict_msh.predict_output(args[1][0])
        iw = ImagePil.open(args[1][0])
        iw.save('./source/image_pred.jpg')
    except IndexError:
        prediction, danger, info = predict_msh.predict_output(args[0][0])
    print(prediction)



    show = Pop()

    popupWindow = Popup(title="Result", size_hint=(None, None), size=(400, 400))

    show.add_widget(Image(source='./source/image_pred.jpg', size_hint=(0.4, 0.4),
                          pos_hint={"x": 0.05, "y": 0.55}))

    show.add_widget(Label(text=prediction, size_hint=(0.6, 0.2), pos_hint={"x": 0.01, "y": 0.87}, font_size=14))
    show.add_widget(Label(text=danger, pos_hint={"x": 0.2, "y": 0.23}, markup=True))
    show.add_widget(Label(text=info, pos_hint={"x": 0.01, "y": 0.10}, text_size=(350, 350), font_size=12))
    popupWindow.content = show
    popupWindow.open()


kv = Builder.load_file("my.kv")


class MyMainApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()
