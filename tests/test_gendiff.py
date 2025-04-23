# tests/test_gendiff.py
import os

from hexlet_code import generate_diff


def get_fixture_path(filename):
    """Генерирует абсолютный путь к файлу фикстуры."""
    # __file__ - это специальная переменная Python,
    # содержит путь к текущему файлу
    current_dir = os.path.dirname(__file__)
    # Соединяем путь к директории теста, папке fixtures и имени файла
    return os.path.join(current_dir, 'fixtures', filename)


def read_fixture(filename):
    """Читает содержимое файла фикстуры."""
    filepath = get_fixture_path(filename)
    # Открываем файл, читаем содержимое,
    # убираем лишние пробелы/переносы по краям
    with open(filepath, 'r') as f:
        return f.read().strip()


def test_flat_json():
    """Тестирует сравнение двух плоских JSON файлов."""
    # Получаем пути к тестовым файлам
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')

    # Читаем ожидаемый результат из файла фикстуры
    expected_result = read_fixture('expected_flat_diff.txt')

    # Вызываем тестируемую функцию с путями к тестовым файлам
    actual_result = generate_diff(filepath1, filepath2)

    # Главная проверка: сравниваем актуальный результат с ожидаемым
    assert actual_result == expected_result
