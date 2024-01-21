from abc import ABC, abstractmethod
from entity.todolist import Todolist

class TodolistRepository(ABC):

    @abstractmethod
    def get_all() -> list[Todolist]:
        pass

    @abstractmethod
    def add(todolist: Todolist) -> None:
        pass

    def remove(number: int) -> bool:
        pass