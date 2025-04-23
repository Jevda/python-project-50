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

    # 3. Добавляем ОПЦИОНАЛЬНЫЙ аргумент для формата вывода
    #    '-f' - короткая форма
    #    '--format' - длинная форма
    #    metavar='FORMAT' - как будет отображаться имя значения в справке
    #    help - описание опции для справки
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
        # По умолчанию argparse сохранит значение в args.format
        # Если опция не указана, args.format будет None
    )

    # 4. Добавляем ОПЦИОНАЛЬНЫЙ аргумент -h / --help (автоматически)

    # 5. Запускаем разбор аргументов, переданных скрипту
    args = parser.parse_args()

    # 6. Пока просто выведем сообщение и значения аргументов (для отладки)
    #    Предупреждение "Local variable 'args' value is not used" все еще может быть,
    #    так как мы пока не используем args.format, args.first_file и args.second_file
    #    для реальной работы.
    print("Parsing arguments complete.")
    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")
    print(f"Selected format: {args.format}") # Выведем выбранный формат


# Стандартная конструкция Python
if __name__ == '__main__':
    # Вызываем нашу главную функцию
    main()
    