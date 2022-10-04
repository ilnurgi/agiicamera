"""
скрин главного окна
"""

__author__ = 'ilnurgi'

import traceback

from android.permissions import Permission

from kivy.core.camera import Camera
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
        app = self.manager.app
        manager = self.manager

        if not app.permissions.get(Permission.CAMERA):
            manager.log_msg('не предоставлены права на камеру')
            return

        if self.camera is not None:
            return

        try:
            self.camera = Camera()
        except Exception as err:
            manager.log_msg('error create camera')
            manager.log_msg(str(err))
            manager.log_msg(traceback.format_exc())
            return

        manager.log_msg('camera created')
        manager.log_msg(str(dir(self.camera)))

        for f in dir(self.camera):
            if f.startswith('_'):
                continue

            try:
                a = getattr(self.camera, f)
                manager.log_to_file(f)
                manager.log_to_file(str(a))
                manager.log_to_file(a.__doc__)
            except Exception as err:
                manager.log_msg(f)
                manager.log_msg(str(err))
                manager.log_msg(traceback.format_exc())
