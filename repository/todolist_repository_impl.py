from entity.todolist import Todolist
from .todolist_repository import TodolistRepository

class TodolistRepositoryImpl(TodolistRepository):
    data: list[Todolist] = []

    def get_all(self) -> list[Todolist]:
        return self.data

    def add(self, todolist: Todolist) -> None:
        self.data.append(todolist)
    
    def remove(self, number: int) -> bool:
        if ((number - 1) >= len(self.data)):
            return False
        
        del self.data[number - 1]
        return True