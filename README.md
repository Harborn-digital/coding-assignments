# FastAPI Clean Architecture – Review Exercise

This repository is a small API for managing users and tasks. It intentionally contains a mix of easy, moderate, and hard issues for a 30-minute review.

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

A separate `ISSUES.md` lists known problems to spot during review.
