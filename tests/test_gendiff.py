# tests/test_gendiff.py
import json
import os

import pytest
import yaml  # Убедись, что импорт есть

# Импортируем основную функцию и парсер
from gendiff import generate_diff
from gendiff.parsers import parse_data


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
    assert actual_result == expected_result


def test_nested_yaml():
    """Тестирует сравнение вложенных YAML файлов."""
    filepath1 = get_fixture_path('nested_file1.yml')
    filepath2 = get_fixture_path('nested_file2.yml')
    expected_result = read_fixture('expected_nested_stylish.txt')
    actual_result = generate_diff(filepath1, filepath2)
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

    actual_result_json = generate_diff(
        filepath1_json, filepath2_json, format_name='plain'
    )
    assert actual_result_json == expected_result

    actual_result_yml = generate_diff(
        filepath1_yml, filepath2_yml, format_name='plain'
    )
    assert actual_result_yml == expected_result
# ----------------------------------


# --- Тест для JSON ФОРМАТА ВЛОЖЕННЫХ СТРУКТУР ---
def test_nested_json_format():
    """Тестирует сравнение вложенных файлов с выводом в json формате."""
    filepath1 = get_fixture_path('nested_file1.json')
    filepath2 = get_fixture_path('nested_file2.json')
    expected_result_str = read_fixture('expected_json_diff.json')
    actual_result_str = generate_diff(filepath1, filepath2, format_name='json')

    expected_obj = json.loads(expected_result_str)
    actual_obj = json.loads(actual_result_str)
    assert actual_obj == expected_obj
# ----------------------------------


# --- Тесты для ошибок парсера ---
def test_parser_file_not_found():
    """Тестирует ошибку FileNotFoundError при парсинге."""
    with pytest.raises(FileNotFoundError):
        parse_data("non_existent/path.json")


def test_parser_invalid_yaml():
    """Тестирует ошибку парсинга для некорректного YAML."""
    invalid_yaml_path = get_fixture_path('invalid.yml')
    # Используем табуляцию (\t), что является ошибкой в YAML
    invalid_yaml_content = "key:\n\tvalue"  # <-- ИЗМЕНЕНИЕ ЗДЕСЬ
    with open(invalid_yaml_path, 'w') as f:
        f.write(invalid_yaml_content)

    with pytest.raises(yaml.YAMLError):
        parse_data(invalid_yaml_path)

    os.remove(invalid_yaml_path)


def test_parser_unsupported_format():
    """Тестирует ошибку для неподдерживаемого формата файла."""
    unsupported_path = get_fixture_path('file.txt')
    with open(unsupported_path, 'w') as f:
        f.write("some text data")

    with pytest.raises(ValueError, match="Unsupported file format: '.txt'"):
        parse_data(unsupported_path)

    os.remove(unsupported_path)
# -----------------------------
