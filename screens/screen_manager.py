"""
менеджер скринов
"""

__author__ = 'ilnurgi'

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

        screens = (
            self.main_screen,
            self.log_screen,
        )
        for screen in screens:
            screen.set_top_bar_screens(*screens)
            self.add_widget(screen)

        self.current = self.main_screen.name

    def log_msg(self, msg: str):
        """
        записывает логи в виджет
        :param msg: текст сообщения
        """
        self.log_screen.log_msg(msg)
