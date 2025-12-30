from storage import load_data,save_data
from tasks import create_task,add_task,remove_task,mark_done,is_empty

tasks = load_data()

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
            tasks = load_data()
            if is_empty(tasks):
                print("Список задач пуст")
                print("Выберите другой пункт")
            else:
                for i, task in enumerate(tasks):
                    status = "✔" if task['done'] else "✘"
                    time = task.get("time","Без времени")
                    print(f'{i}.{task["name"]} [{time}] {status}')
        elif otvet == "2":
            print("Добавить задачи")
        elif otvet == "3":
            print("Отметить задачи выполненной")
        elif otvet == "4":
            print("Удалить задачи")
        else:
            print("Не корректный выбор,повторите попытку")
if __name__ == "__main__":
    main()