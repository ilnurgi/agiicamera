"""
менеджер скринов
"""

__author__ = 'ilnurgi'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

from screens.log_screen import LogScreen
from screens.main_screen import MainScreen


class AppScreenManager(ScreenManager):
    """
    менеджер скринов
    """

    def __init__(self):
        """
        инициализация
        """
        super().__init__()

        self.transition = NoTransition()

        self.main_screen = MainScreen()
        self.log_screen = LogScreen()
        self.app = App.get_running_app()

        screens = (
            self.main_screen,
            self.log_screen,
        )
        for screen in screens:
            screen.set_top_bar_screens(*screens)
            self.add_widget(screen)

        self.current = self.main_screen.name

    def log_msg(self, msg: str, log_to_file: bool = True):
        """
        записывает логи в виджет
        :param msg: текст сообщения
        :param log_to_file: логировать в файл
        """
        self.log_screen.log_msg(msg, log_to_file)

    def log_to_file(self, text: str):
        """
        записывает логи в файл
        :param text: текст сообщения
        """
        self.log_screen.log_to_file(text)
