.PHONY: dev run migrate migrate-create fix qa test

dev:
	@echo "Starting development environment..."
	@docker compose up

migrate:
	@echo "Running migrations in backend..."
	@docker compose exec -T backend alembic upgrade head

migrate-create:
	@echo "Creating new migration in backend..."
	@docker compose exec backend alembic revision --autogenerate -m "$(msg)"

fix:
	@echo "Running ruff fixes..."
	@uv run ruff check --fix .
	@uv run ruff format .

qa:
	@echo "Running quality checks..."
	@uv run ruff check .
	@uv run mypy app data domain services
