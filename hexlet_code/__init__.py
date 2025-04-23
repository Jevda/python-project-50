# hexlet_code/__init__.py

# Импортируем основную функцию из модуля differ
from .differ import generate_diff

# Объявляем, что именно экспортируется из пакета при импорте "звездочкой"
# (from hexlet_code import *) и для документации.
__all__ = ('generate_diff',)
