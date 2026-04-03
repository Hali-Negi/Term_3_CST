import abc
from logging import Handler


class Handler(abc.ABC):

    def __init__(self, next_handler = None):
        self.next_handler = next_handler

    def set_next(self, handler):
        self.next_handler = handler

    @abc.abstractmethod
    def next(self, request):
        ...
