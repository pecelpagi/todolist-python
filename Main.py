from repository.todolist_repository import TodolistRepository
from repository.todolist_repository_impl import TodolistRepositoryImpl
from service.todolist_service import TodolistService
from service.todolist_service_impl import TodolistServiceImpl
from view.todolist_view import TodolistView

todolist_repository: TodolistRepository = TodolistRepositoryImpl()
todolist_service: TodolistService = TodolistServiceImpl(todolist_repository)
todolist_view: TodolistView = TodolistView(todolist_service)

todolist_view.show_todolist()