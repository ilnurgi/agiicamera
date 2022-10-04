"""
AGiiCamera
"""

__author__ = 'ilnurgi'

import traceback

from typing import List

from android.permissions import Permission, request_permissions
from android.storage import primary_external_storage_path, app_storage_path

from kivy.app import App

from screens.screen_manager import AppScreenManager


class AGiiCameraApp(App):
    """
    приложение
    """

    def __init__(self):
        """
        инициализация
        """
        super().__init__()

        self.app_name = 'agiicamera'
        self.camera = None
        self.permissions = {}

        self.screen_manager = AppScreenManager()
        self.public_storage = primary_external_storage_path()
        self.internal_storage = app_storage_path()

    def build(self):
        """
        билд приложения
        """

        self.screen_manager.log_msg('app build', log_to_file=False)
        try:
            request_permissions(
                [
                    Permission.CAMERA,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.WRITE_EXTERNAL_STORAGE
                ],
                self.permission_callback,
            )
        except Exception as err:
            self.screen_manager.log_msg('permission error')
            self.screen_manager.log_msg(str(err))
            self.screen_manager.log_msg(traceback.format_exc())
        else:
            self.screen_manager.log_msg('permission granted', log_to_file=False)

        return self.screen_manager

    def permission_callback(self, permissions: List[str], permissions_result: List[bool]):
        """
        колбек для запроса по правам
        """
        self.screen_manager.log_msg(
            f'{permissions}, {permissions_result}',
            log_to_file=False,
        )
        for permission, permission_grant in zip(permissions, permissions_result):
            self.permissions[permission] = permission_grant


if __name__ == '__main__':
    AGiiCameraApp().run()
