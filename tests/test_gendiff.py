# tests/test_gendiff.py
import os

from hexlet_code import generate_diff


# --- Вспомогательные функции ---
def get_fixture_path(filename):
    """Генерирует абсолютный путь к файлу фикстуры."""
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_fixture(filename):
    """Читает содержимое файла фикстуры."""
    filepath = get_fixture_path(filename)
    with open(filepath, 'r') as f:
        return f.read()
# -----------------------------


# --- Тесты для плоских файлов ---
def test_flat_json():
    """Тестирует сравнение двух плоских JSON файлов."""
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')
    expected_result = read_fixture('expected_flat_diff.txt')
    actual_result = generate_diff(filepath1, filepath2)
    assert actual_result == expected_result


def test_flat_yaml():
    """Тестирует сравнение двух плоских YAML файлов."""
    filepath1 = get_fixture_path('file1.yml')
    filepath2 = get_fixture_path('file2.yml')
    expected_result = read_fixture('expected_flat_diff.txt')
    actual_result = generate_diff(filepath1, filepath2)
    assert actual_result == expected_result
# ----------------------------------


# --- Тесты для вложенных структур ---
def test_nested_json():
    """Тестирует сравнение вложенных JSON файлов."""
    filepath1 = get_fixture_path('nested_file1.json')
    filepath2 = get_fixture_path('nested_file2.json')
    expected_result = read_fixture('expected_nested_stylish.txt')
    actual_result = generate_diff(filepath1, filepath2)

    # Отладочная печать (можно будет убрать позже)
    if actual_result != expected_result:
        try:
            with open(
                "actual_output_json.txt", "w", encoding='utf-8'
            ) as f_actual:
                f_actual.write(actual_result)
            print("\nDEBUG: Actual output saved to actual_output_json.txt")
        except Exception as e:
            print(f"\nDEBUG: Failed to write actual output: {e}")
        print("\n--- EXPECTED (nested_json - stylish) ---")
        print(repr(expected_result))
        print("--- ACTUAL (nested_json - stylish) ---")
        print(repr(actual_result))
        print("--- END (nested_json - stylish) ---")

    assert actual_result == expected_result


def test_nested_yaml():
    """Тестирует сравнение вложенных YAML файлов."""
    filepath1 = get_fixture_path('nested_file1.yml')
    filepath2 = get_fixture_path('nested_file2.yml')
    expected_result = read_fixture('expected_nested_stylish.txt')
    actual_result = generate_diff(filepath1, filepath2)

    # Отладочная печать (можно будет убрать позже)
    if actual_result != expected_result:
        try:
            with open(
                "actual_output_yaml.txt", "w", encoding='utf-8'
            ) as f_actual:
                f_actual.write(actual_result)
            print("\nDEBUG: Actual output saved to actual_output_yaml.txt")
        except Exception as e:
            print(f"\nDEBUG: Failed to write actual output: {e}")
        print("\n--- EXPECTED (nested_yaml - stylish) ---")
        print(repr(expected_result))
        print("--- ACTUAL (nested_yaml - stylish) ---")
        print(repr(actual_result))
        print("--- END (nested_yaml - stylish) ---")

    assert actual_result == expected_result
# -------------------------------------------


# --- Тест для PLAIN ФОРМАТА ВЛОЖЕННЫХ СТРУКТУР ---
def test_nested_plain_format():
    """Тестирует сравнение вложенных файлов с выводом в plain формате."""
    filepath1_json = get_fixture_path('nested_file1.json')
    filepath2_json = get_fixture_path('nested_file2.json')
    filepath1_yml = get_fixture_path('nested_file1.yml')
    filepath2_yml = get_fixture_path('nested_file2.yml')

    expected_result = read_fixture('expected_plain_diff.txt')

    # ИСПРАВЛЕНО E501: Перенос строки
    actual_result_json = generate_diff(
        filepath1_json, filepath2_json, format_name='plain'
    )
    # Отладочная печать для JSON -> plain
    if actual_result_json != expected_result:
        print("\n--- EXPECTED (nested_json - plain) ---")
        print(repr(expected_result))
        print("--- ACTUAL (nested_json - plain) ---")
        print(repr(actual_result_json))
        print("--- END (nested_json - plain) ---")
    assert actual_result_json == expected_result

    # ИСПРАВЛЕНО E501: Перенос строки
    actual_result_yml = generate_diff(
        filepath1_yml, filepath2_yml, format_name='plain'
    )
    # Отладочная печать для YAML -> plain
    if actual_result_yml != expected_result:
        print("\n--- EXPECTED (nested_yaml - plain) ---")
        print(repr(expected_result))
        print("--- ACTUAL (nested_yaml - plain) ---")
        print(repr(actual_result_yml))
        print("--- END (nested_yaml - plain) ---")
    assert actual_result_yml == expected_result


# ----------------------------------
# --- НОВЫЙ ТЕСТ ДЛЯ JSON ФОРМАТА ---
def test_nested_json_format():
    """Тестирует сравнение вложенных файлов с выводом в json формате."""
    filepath1 = get_fixture_path('nested_file1.json')
    filepath2 = get_fixture_path('nested_file2.json')
    # Ожидаемый результат читаем из нового .json файла фикстуры
    # Важно: читаем как текст, сравнивать будем тоже текст
    expected_result = read_fixture('expected_json_diff.json')

    # Вызываем generate_diff, явно указывая формат 'json'
    actual_result = generate_diff(filepath1, filepath2, format_name='json')

    # Сравниваем актуальный JSON-строку с ожидаемой JSON-строкой
    # Может понадобиться парсить обе строки в json и сравнивать объекты,
    # если форматирование (отступы) может отличаться, но пока сравним строки
    assert actual_result == expected_result
# ----------------------------------
