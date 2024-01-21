from abc import ABC, abstractmethod

class TodolistService(ABC):

    @abstractmethod
    def show_todolist() -> None:
        pass

    @abstractmethod
    def add_todolist(todo: str) -> None:
        pass

    @abstractmethod
    def remove_todolist(number: int) -> None:
        pass