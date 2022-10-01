"""
скрин с логами
"""

__author__ = 'ilnurgi'

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

    def log_msg(self, msg: str):
        """
        записывает логи в виджет
        :param msg: текст сообщения
        """
        self.text_label.text = f'{self.text_label.text}\n{msg}'

        self.text_label.texture_update()
        self.text_label.size = self.text_label.texture_size

        self.scroll_view.scroll_y = 0
