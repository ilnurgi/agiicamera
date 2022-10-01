"""
базовый скрин с топбаром
"""

__author__ = 'ilnurgi'

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from screens.helpers import error


class BaseScreen(Screen):
    """
    базовый скрин
    """

    @error
    def __init__(self):
        """
        инициализация
        """
        super().__init__()

        self.screen_container = BoxLayout(
            orientation='vertical',
        )
        self.add_widget(self.screen_container)

        self.top_bar_screens = {}

        self._init_top_bar()
        self._init_content()

    @error
    def _init_top_bar(self):
        """
        инициализация топ бара
        """

        self.top_bar_container = BoxLayout(
            orientation='horizontal',
            size_hint_y=0.1,
            padding=10,
            spacing=10,
        )
        self.screen_container.add_widget(self.top_bar_container)

    @error
    def _init_content(self):
        """
        инициализация контента
        """

        self.content_container = BoxLayout(
            orientation='vertical',
            padding=10,
        )
        self.screen_container.add_widget(self.content_container)

    @error
    def set_top_bar_screens(self, *screens):
        """
        формируем топ бар
        """

        for screen in screens:
            top_bar_button = Button(
                text=screen.title,
            )
            if self == screen:
                top_bar_button.background_normal = top_bar_button.background_down

            top_bar_button.bind(on_press=self.change_screen)

            self.top_bar_container.add_widget(top_bar_button)

            self.top_bar_screens[screen.title] = screen

    @error
    def change_screen(self, button):
        """
        обработчик изменения скрина
        :param button: кнопка изменения
        """
        screen = self.top_bar_screens[button.text]
        self.manager.current = screen.name
