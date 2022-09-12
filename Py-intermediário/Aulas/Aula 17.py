"""
Faça uma task list com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última opção)
    opção de refazer (a cada vez que chamarmos, refaz a última opção)
"""
from time import sleep


def show_op(todo_list):
    print('Tarefas: ')
    print(todo_list)


def do_add(todo, todo_list):
    todo_list.append(todo)


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a desfazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)

if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls, exit: ')

        if todo == 'ls':
            show_op(todo_list)
            continue

        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue

        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue
        elif todo == 'exit':
            print('Saindo...')
            sleep(1)
            exit(1)
        do_add(todo, todo_list)
