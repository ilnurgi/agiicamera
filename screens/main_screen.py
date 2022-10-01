"""
скрин главного окна
"""

__author__ = 'ilnurgi'

import traceback

from android.permissions import Permission

from kivy.app import App
from kivy.uix.button import Button

from screens.base_screen import BaseScreen
from screens.helpers import error


class MainScreen(BaseScreen):
    """
    главный скрин
    """

    @error
    def __init__(self):
        """
        иницализация
        """
        super().__init__()

        self.name = 'main_screen'
        self.title = 'MAIN'
        self.camera = None

    @error
    def _init_content(self):
        """
        заполнение контента
        """
        super()._init_content()

        btn_create_camera = Button(
            text='Создать камеру'
        )
        btn_create_camera.bind(on_press=self.create_camera)

        self.content_container.add_widget(btn_create_camera)

    @error
    def create_camera(self, button):
        """
        создание камеры
        :param button: кнопка, создавшая камеру
        """
        app = App.get_running_app()

        if not app.permissions.get(Permission.CAMERA):
            self.manager.log_msg('не предоставлены права на камеру')
            return

        try:
            from kivy.uix.camera import Camera
        except Exception as err:
            self.manager.log_msg('error import camera')
            self.manager.log_msg(str(err))
            self.manager.log_msg(traceback.format_exc())
        else:
            self.manager.log_msg('camera imported')
            try:
                self.camera = Camera()
            except Exception as err:
                self.manager.log_msg('error create camera')
                self.manager.log_msg(str(err))
                self.manager.log_msg(traceback.format_exc())
            else:
                self.manager.log_msg('camera created')
