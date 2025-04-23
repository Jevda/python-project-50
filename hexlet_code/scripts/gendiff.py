# Импортируем модуль argparse для работы с аргументами командной строки
import argparse
# Импортируем модуль sys для доступа к stderr и exit
import sys
# Импортируем модуль json для парсинга JSON-файлов
import json


# --- Функция для загрузки данных ---
def load_data(filepath):
    """Загружает данные из JSON-файла по указанному пути."""
    try:
        # Открываем файл на чтение в кодировке UTF-8
        # 'with' гарантирует закрытие файла после использования
        with open(filepath, 'r', encoding='utf-8') as f:
            # Парсим JSON напрямую из файлового объекта
            data = json.load(f)
            return data
    except FileNotFoundError:
        # Обработка ошибки: файл не найден
        # Переносим длинную f-строку для < 80 символов
        error_message = f"Error: File not found at '{filepath}'"
        print(error_message, file=sys.stderr)
        # Завершаем программу с кодом ошибки 1
        sys.exit(1)
    except json.JSONDecodeError:
        # Обработка ошибки: файл содержит некорректный JSON
        # Переносим длинную f-строку
        error_message = f"Error: Could not decode JSON from file '{filepath}'"
        print(error_message, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Обработка других возможных ошибок чтения/доступа к файлу
        # Переносим длинную f-строку
        error_message = (
            f"An error occurred while reading file '{filepath}': {e}"
        )
        print(error_message, file=sys.stderr)
        sys.exit(1)


def main():
    # 1. Создаем парсер аргументов
    # Переносим длинную строку description с помощью скобок
    parser = argparse.ArgumentParser(
        description=(
            'Compares two configuration files and shows a difference.'
        )
    )

    # 2. Добавляем позиционные аргументы (пути к файлам)
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # 3. Добавляем опциональный аргумент для формата
    # Эта строка, скорее всего, уже была < 80 символов
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
    )

    # 4. Парсим аргументы командной строки
    args = parser.parse_args()

    # 5. ЧТЕНИЕ И ПАРСИНГ ФАЙЛОВ
    # Получаем пути из аргументов
    filepath1 = args.first_file
    filepath2 = args.second_file

    # Загружаем данные из файлов с помощью нашей функции
    data1 = load_data(filepath1)
    data2 = load_data(filepath2)

    # 6. Выводим результат парсинга (пока для проверки)
    print("Data loaded successfully!")
    print("Data from first file:")
    print(data1)
    print("\nData from second file:")
    print(data2)

    # Выведем также выбранный формат (если он был передан)
    if args.format:
        print(f"\nOutput format selected: {args.format}")
    else:
        # Переносим длинную строку с помощью неявной конкатенации
        print(
            "\nOutput format not specified (will use default later)."
        )


# Стандартная конструкция Python
if __name__ == '__main__':
    main()
