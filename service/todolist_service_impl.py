from .todolist_service import TodolistService
from repository.todolist_repository import TodolistRepository
from entity.todolist import Todolist

class TodolistServiceImpl(TodolistService):

    __todolist_repository: TodolistRepository = None

    def __init__(self, todolist_repository: TodolistRepository) -> None:
        self.__todolist_repository = todolist_repository

    def show_todolist(self) -> None:
        collections: list(Todolist) = self.__todolist_repository.get_all()

        print("TODOLIST")
        for index, collection in enumerate(collections):
            todolist = collection
            num = index + 1

            print(str(num) + ". " + todolist.get_todo())

    def add_todolist(self, todo: str) -> None:
        todolist = Todolist(todo)
        self.__todolist_repository.add(todolist)
        print("SUKSES MENAMBAH TODO : " + todo)
    
    def remove_todolist(self, number: int) -> None:
        success: bool = self.__todolist_repository.remove(number)

        if (success):
            print("SUKSES MENGHAPUS TODO : " + str(number))
        else:
            print("GAGAL MENGHAPUS TODO : " + str(number))