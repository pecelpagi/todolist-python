from service.todolist_service import TodolistService

class TodolistView:

    __todolist_service: TodolistService = None

    def __init__(self, todolist_service: TodolistService) -> None:
        self.__todolist_service = todolist_service

    def show_todolist(self) -> None:
        while (True):
            self.__todolist_service.show_todolist()

            print("MENU : ")
            print("1. Tambah")
            print("2. Hapus")
            print("x. Keluar")

            input_value = input("Pilih : ")

            if (input_value == "1"):
                self.add_todolist()
            elif (input_value == "2"):
                self.remove_todolist()
            elif (input_value == "x"):
                break
            else:
                print("Pilihan tidak dimengerti")

    def add_todolist(self) -> None:
        print("MENAMBAH TODOLIST")

        todo = input("Todo (x Jika Batal) : ")

        if (todo == "x"):
            pass
        else:
            self.__todolist_service.add_todolist(todo)

    def remove_todolist(self) -> None:
        print("MENGHAPUS TODOLIST")

        number = int(input("Nomor yang Dihapus (x Jika Batal) : "))

        if (number == "x"):
            pass
        else:
            self.__todolist_service.remove_todolist(number)