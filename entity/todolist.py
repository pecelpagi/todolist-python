class Todolist:

    __todo = None

    def __init__(self, todo: str) -> None:
        self.__todo = todo

    def get_todo(self):
        return self.__todo
    
    def set_todo(self, todo):
        self.__todo = todo