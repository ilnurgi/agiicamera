"""
скрин главного окна
"""

__author__ = 'ilnurgi'

import os
import traceback
from datetime import datetime

from android.permissions import Permission

from kivy.core.camera import Camera
from kivy.core.image import Texture
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
        self.camera_texture: Texture = None

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

        btn_get_photo = Button(
            text='Сохранить фотку'
        )
        btn_get_photo.bind(on_press=self.get_photo)

        self.content_container.add_widget(btn_create_camera)
        self.content_container.add_widget(btn_get_photo)

    @error
    def on_camera_texture(self, camera):
        self.camera_texture = camera.texture
        # self.manager.log_msg('on_tex')
        # self.manager.log_msg(type(camera.texture))
        # self.manager.log_msg(camera.texture)

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

        manager.log_msg(type(self.camera.texture))
        manager.log_to_file(str(self.camera.texture))

        self.camera.bind(on_texture=self.on_camera_texture)

    def get_photo(self, button):
        self.manager.log_msg(self.camera_texture)
        if not self.camera_texture:
            return

        app = self.manager.app

        log_file_name = f'{app.app_name}_{datetime.now()}.png'
        log_file_path = os.path.join(app.public_storage, log_file_name)
        self.camera_texture.save(log_file_path)
