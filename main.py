from storage import load_data,save_data
from tasks import create_task,add_task,remove_task,mark_done,is_empty

def show_menu():
    print('\nМеню:')
    print('1. Показать задачи')
    print('2. Добавить задачи')
    print('3. Отметить задачу выполненной')
    print('4. Удалить задачи')
    print('0. Выход')
def main(): 
    while True:
        show_menu()
        otvet = input("Выберите пункт: ")
        if otvet == "0":
            print("Программа завершена")
            break
        elif otvet == "1":
            print('Показать задачи')
        elif otvet == "2":
            print("Добавить задачи")
        elif otvet == "3":
            print("Отметить задачи выполненной")
        elif otvet == "4":
            print("Удалить задачи")
        else:
            print("Не корректный выбор,повторите попытку")