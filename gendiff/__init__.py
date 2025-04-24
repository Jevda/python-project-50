# gendiff/__init__.py

# Импортируем основную функцию из модуля differ (относительный импорт)
from .differ import generate_diff

# Объявляем экспорт
__all__ = ('generate_diff',)