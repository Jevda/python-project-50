# gendiff/formatters/__init__.py
# Относительные импорты не меняются
from .json import format_json
from .plain import format_plain
from .stylish import format_stylish

# Словарь, связывающий имя формата с функцией форматирования
FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def get_formatter(format_name):
    """Возвращает функцию форматирования по имени или вызывает ошибку."""
    if format_name in FORMATTERS:
        return FORMATTERS[format_name]
    else:
        supported_formats = ", ".join(FORMATTERS.keys())
        raise ValueError(
            f"Unsupported format: '{format_name}'. "
            f"Supported formats: {supported_formats}"
        )


# Экспортируем только нужную функцию или словарь
__all__ = ('get_formatter', 'format_stylish', 'format_plain', 'format_json')