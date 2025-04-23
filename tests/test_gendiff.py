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

    if actual_result != expected_result:
        try:
            # ИСПРАВЛЕНО: Перенос строки для with open
            with open(
                "actual_output_json.txt", "w", encoding='utf-8'
            ) as f_actual:
                f_actual.write(actual_result)
            print("\nDEBUG: Actual output saved to actual_output_json.txt")
        except Exception as e:
            print(f"\nDEBUG: Failed to write actual output: {e}")
        print("\n--- EXPECTED (nested_json) ---")
        print(repr(expected_result))
        print("--- ACTUAL (nested_json) ---")
        print(repr(actual_result))
        print("--- END (nested_json) ---")

    assert actual_result == expected_result


def test_nested_yaml():
    """Тестирует сравнение вложенных YAML файлов."""
    filepath1 = get_fixture_path('nested_file1.yml')
    filepath2 = get_fixture_path('nested_file2.yml')
    expected_result = read_fixture('expected_nested_stylish.txt')
    actual_result = generate_diff(filepath1, filepath2)

    if actual_result != expected_result:
        try:
            # ИСПРАВЛЕНО: Перенос строки для with open
            with open(
                "actual_output_yaml.txt", "w", encoding='utf-8'
            ) as f_actual:
                f_actual.write(actual_result)
            print("\nDEBUG: Actual output saved to actual_output_yaml.txt")
        except Exception as e:
            print(f"\nDEBUG: Failed to write actual output: {e}")
        print("\n--- EXPECTED (nested_yaml) ---")
        print(repr(expected_result))
        print("--- ACTUAL (nested_yaml) ---")
        print(repr(actual_result))
        print("--- END (nested_yaml) ---")

    assert actual_result == expected_result
# -------------------------------------------
