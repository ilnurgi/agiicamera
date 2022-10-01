"""
хелперы
"""

__author__ = 'ilnurgi'

import functools
import traceback


def error(func):
    """
    перехват исключений и отправка в логи
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            args[0].manager.log_msg(str(err))
            args[0].manager.log_msg(traceback.format_exc())

    return inner
