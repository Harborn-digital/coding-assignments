# FastAPI Clean Architecture – Review Exercise

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Optional seed data:
```bash
python app/scripts/seed.py
```

Structure roughly follows a clean architecture layering:
- `domain` for core entities
- `schemas` for API I/O models
- `services` for business logic
- `infrastructure` for database and repositories
- `api` for transport layer (FastAPI routes)
- `core` for config and security

