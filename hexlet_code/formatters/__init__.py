# hexlet_code/formatters/__init__.py
from .plain import format_plain
from .stylish import format_stylish

# from .json import format_json # Задел на будущее

# Словарь, связывающий имя формата с функцией форматирования
FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    # 'json': format_json,
}


def get_formatter(format_name):
    """Возвращает функцию форматирования по имени или вызывает ошибку."""
    if format_name in FORMATTERS:
        return FORMATTERS[format_name]
    else:
        # Если формат не найден, выбрасываем ошибку
        supported_formats = ", ".join(FORMATTERS.keys())
        raise ValueError(
            f"Unsupported format: '{format_name}'. "
            f"Supported formats: {supported_formats}"
        )


# Экспортируем только нужную функцию или словарь
__all__ = ('get_formatter',)