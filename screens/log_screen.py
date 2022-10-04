"""
скрин с логами
"""

__author__ = 'ilnurgi'

import os

from datetime import datetime

from android.permissions import Permission

from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from screens.base_screen import BaseScreen
from screens.helpers import error


class LogScreen(BaseScreen):
    """
    скрин с логами
    """

    @error
    def __init__(self):
        """
        инициализация
        """
        super().__init__()

        self.name = 'log_screen'
        self.title = 'LOG'
        self.__msg_lines = []
        self.__screen_init_dt = datetime.now()
        self.__log_text_lines = []
        self.__max_log_text_lines = 1

    @error
    def _init_content(self):
        """
        заполнение контента
        """
        super()._init_content()

        self.text_label = Label(
            size_hint_y=None,
            size_hint_x=None,
        )

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.text_label)

        self.content_container.add_widget(self.scroll_view)

    def log_msg(self, msg: str, log_to_file: bool = True):
        """
        записывает логи в виджет
        :param msg: текст сообщения
        :param log_to_file: логировать в файл
        """
        msg = str(msg)

        if log_to_file:
            self.log_to_file(msg)

        len_msg = len(msg)
        max_len = 70
        if len_msg > max_len:
            msg_lines = [
                msg[(pos*max_len):(pos*max_len)+max_len]
                for pos in range(int(len_msg / max_len) + 1)
            ]
            self.__msg_lines.extend(msg_lines)
        else:
            self.__msg_lines.append(msg)

        self.__msg_lines = self.__msg_lines[-70:]
        self.text_label.text = '\n'.join(self.__msg_lines)

        self.text_label.texture_update()
        self.text_label.size = self.text_label.texture_size

        self.scroll_view.scroll_y = 0

    def log_to_file(self, text: str):
        """
        логирует текст в файл
        :param text: текст
        """
        text = str(text)

        app = self.manager.app

        if not app.permissions.get(Permission.WRITE_EXTERNAL_STORAGE):
            self.log_msg('не хватает прав WRITE_EXTERNAL_STORAGE для записи файла лога', log_to_file=False)
            return
        if not app.permissions.get(Permission.READ_EXTERNAL_STORAGE):
            self.log_msg('не хватает прав READ_EXTERNAL_STORAGE для чтения файла лога', log_to_file=False)
            return

        self.__log_text_lines.append(text)
        if len(self.__log_text_lines) < self.__max_log_text_lines:
            return

        log_file_name = f'{app.app_name}_{self.__screen_init_dt}.log'
        log_file_path = os.path.join(app.public_storage, log_file_name)
        with open(log_file_path, 'a') as log_file:
            log_file.write('\n'.join(self.__log_text_lines))
        self.__log_text_lines.clear()
