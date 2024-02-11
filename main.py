import os
from typing import List, Tuple


def print_records(records: List[Tuple[str]], page_size: int, page_num: int) -> None:
    """Функция для вывода записей из справочника постранично"""
    
    start = (page_num - 1) * page_size
    end = start + page_size
    total_pages = (len(records) + page_size - 1) // page_size

    for i, record in enumerate(records[start:end]):
        print(f"{i+start+1}. {record}")

    if total_pages == 1:
        return

    print()
    print(f"Страница {page_num}/{total_pages}")
    print()

    if page_num > 1:
        print("1. Предыдущая страница")
    if page_num < total_pages:
        print("2. Следующая страница")
    if page_num > 1 or page_num < total_pages:
        print("Любой другой символ для выхода в основное меню")

    choice = input("Выберите действие: ")
    print()

    if choice == "1" and page_num > 1:
        page_num -= 1
        print_records(records, page_size, page_num)
    elif choice == "2" and page_num < total_pages:
        page_num += 1
        print_records(records, page_size, page_num)
    elif choice == "3":
        return


def add_record(records: List[Tuple[str]]) -> None:
    """Функция для добавления новой записи в справочник"""

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    organization = input("Введите название организации: ")
    work_phone = input("Введите рабочий телефон: ")
    personal_phone = input("Введите личный телефон: ")
    records.append((surname, name, patronymic, organization, work_phone, personal_phone))


def edit_record(records: List[Tuple[str]], index: int) -> None:
    """Функция для редактирования записи в справочнике"""

    surname = input("Введите новую фамилию: ")
    name = input("Введите новое имя: ")
    patronymic = input("Введите новое отчество: ")
    organization = input("Введите новое название организации: ")
    work_phone = input("Введите новый рабочий телефон: ")
    personal_phone = input("Введите новый личный телефон: ")
    records[index] = (surname, name, patronymic, organization, work_phone, personal_phone)


def search_records(records: List[Tuple[str]], attributes: List[str]) -> List[Tuple[str]]:
    """Функция для поиска записей по характеристикам"""

    search_results = []
    for record in records:
        if all(attr in record for attr in attributes):
            search_results.append(record)
    return search_results


def save_records(records: List[Tuple[str]], filename: str) -> None:
    """Функция для сохранения записей в текстовый файл"""

    with open(filename, "w") as file:
        for record in records:
            file.write(",".join(record) + "\n")


def load_records(filename: str) -> List[Tuple[str]]:
    """Функция для загрузки записей из текстового файла"""

    records = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                record = line.strip().split(",")
                records.append(tuple(record))
    return records


def main() -> None:
    """Основная функция программы"""

    filename = "справочник.txt"
    records = load_records(filename)
    page_size = 5
    page_num = 1

    while True:
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            print_records(records, page_size, page_num)

        elif choice == "2":
            add_record(records)
            save_records(records, filename)
            print("Запись добавлена")

        elif choice == "3":
            index = int(input("Введите индекс записи для редактирования: ")) - 1
            if index >= 0 and index < len(records):
                edit_record(records, index)
                save_records(records, filename)
                print("Запись сохранена")
            else:
                print("Неверный индекс записи")

        elif choice == "4":
            attributes = input(
                "Введите через запятую без пробелов характеристики для поиска: "
            ).split(",")
            results = search_records(records, attributes)
            print("Результаты поиска:")
            print_records(results, page_size, page_num)

        elif choice == "5":
            break

        else:
            print("Неверный выбор")

        print()


if __name__ == '__main__':
    main()
