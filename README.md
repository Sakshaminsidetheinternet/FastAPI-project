# FastAPI Learning Project — Patient API

A learning project exploring how to build REST endpoints with FastAPI and validate request data using Pydantic models.

## Overview

The main API file defines a patient data model with fields such as name, city, age, gender, height and weight. Pydantic computed fields calculate BMI and a basic category from the supplied measurements. The application also explores create, read, update and sort-style API routes backed by a local JSON file.

## Technology

- Python
- FastAPI
- Pydantic
- JSON file persistence

## Run locally

```bash
git clone https://github.com/Sakshaminsidetheinternet/FastAPI-project.git
cd FastAPI-project
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
```

Open the interactive API documentation at http://127.0.0.1:8000/docs.

## Concepts explored

- Defining Pydantic request models.
- Field validation and constraints.
- Computed fields.
- Query and path parameters.
- HTTP error responses.
- Basic JSON-backed CRUD patterns.

## Current status and limitations

This is a learning repository, not a production patient-record system. The inspected source contains unfinished/inconsistent areas (including JSON import/persistence and update logic), so some routes may need correction before they run end-to-end. It uses local JSON storage and has no authentication, authorisation, audit trail or privacy controls. Do not use it with real patient or other sensitive personal data.

## Demo and screenshots

No public deployment or screenshots are currently linked. The local FastAPI Swagger UI at `/docs` is the easiest way to explore the endpoints after resolving any runtime issues.

## Author

**Saksham Gupta** — [GitHub](https://github.com/Sakshaminsidetheinternet)
