from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyPaintApp(App):
    def build(self):
        v_box_layout = BoxLayout(
            orientation='vertical',
        )

        text = TextInput()
        v_box_layout.add_widget(text)

        button = Button(
            text='Кнопка',
        )
        v_box_layout.add_widget(button)

        try:
            from kivy.uix.camera import Camera
        except Exception as err:
            import traceback
            text.text = (
                f'{err}'
                f'{traceback.format_exc()}'
            )

        else:
            text.text = 'import done'

        try:
            cam = Camera()
        except Exception as err:
            import traceback
            text.text = (
                f'{err}'
                f'{traceback.format_exc()}'
            )
        else:
            text.text = 'Camera() done'

        return v_box_layout


if __name__ == '__main__':
    MyPaintApp().run()
