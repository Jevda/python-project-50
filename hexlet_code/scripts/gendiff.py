# Импортируем модуль argparse для работы с аргументами командной строки
import argparse
# Импортируем модуль sys (может понадобиться для sys.exit, stderr)
import sys

# Определяем главную функцию, где будет основная логика
def main():
    # 1. Создаем парсер аргументов
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # 2. Добавляем ОБЯЗАТЕЛЬНЫЕ (позиционные) аргументы
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')

    # 3. Добавляем ОПЦИОНАЛЬНЫЙ аргумент -h / --help (автоматически)

    # 4. Запускаем разбор аргументов, переданных скрипту
    args = parser.parse_args()

    # 5. Пока просто выведем сообщение, что парсинг прошел
    #    Предупреждение "Local variable 'args' value is not used" здесь ожидаемо.
    print("Parsing arguments complete. Ready to compare files (logic not implemented yet).")


# Стандартная конструкция Python
if __name__ == '__main__':
    # Вызываем нашу главную функцию
    main()
