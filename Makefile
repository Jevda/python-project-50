# Makefile для проекта Gendiff

# Цель для установки всех зависимостей, включая dev-зависимости
install:
	uv pip sync --dev

# Цель для запуска линтера Ruff через 'uv run'
lint:
	uv run ruff check . # <-- Добавлено 'uv run'

# Цель для запуска тестов с помощью pytest через 'uv run'
test:
	uv run pytest # <-- Добавлено 'uv run'

# Цель для запуска тестов с покрытием через 'uv run'
test-coverage:
	uv run pytest --cov=hexlet_code --cov-report xml # <-- Добавлено 'uv run'

# Цель для полной проверки: сначала линтер, потом тесты
check:
	make lint
	make test

# Цель для сборки пакета
build:
	uv build

# Цель для очистки временных файлов
clean:
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -f coverage.xml
	rm -rf *.egg-info/
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

# Специальная цель .PHONY
.PHONY: install lint test test-coverage check build clean