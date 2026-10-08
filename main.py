
from zd_1_list import task1_with_list
from zd_2_list import task2_with_list
from zd_1_without_a_list import task1_without_list
from zd_2_without_a_list import task2_without_list

def main():
    print("=== МЕНЮ ===")
    print("1 — Задача 1 (со списком)")
    print("2 — Задача 1 (без списка)")
    print("3 — Задача 2 (со списком)")
    print("4 — Задача 2 (без списка)")
    
    choice = input("Выберите вариант (1-4): ").strip()

    if choice == "1":
        task1_with_list()
    elif choice == "2":
        task1_without_list()
    elif choice == "3":
        task2_with_list()
    elif choice == "4":
        task2_without_list()
    else:
        print("Неверный выбор. Запустите программу снова и введите число от 1 до 4.")

if __name__ == "__main__":
    main()
