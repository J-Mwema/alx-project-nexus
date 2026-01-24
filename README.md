# Job Board Platform — Backend (Project Nexus)

## Status
- ✅ Core models implemented: `User` (custom), `Job`, `Application`
- ✅ JWT authentication (SimpleJWT) with register/login/refresh endpoints
- ✅ Jobs CRUD endpoints (list/create/retrieve/update/delete)
- ✅ Applications endpoints (apply, update status)
- ✅ Manual end-to-end tests executed locally (register, login, create job, apply, accept)

## Project Summary
This repository implements the backend for a Job Board platform using Django and Django REST Framework. It supports role-based access control (Admin / Employer / Job Seeker), job posting and management, and applications with status tracking.

## Quick start
1. Create and activate a virtualenv, then install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run migrations and start the server:

   ```bash
   cd backend
   python3 manage.py migrate
   python3 manage.py runserver 0.0.0.0:8000
   ```

## Key API endpoints (examples)
- Register: POST `/api/auth/register/` (payload: `username`, `email`, `password`, `first_name`, `last_name`)
- Login (JWT): POST `/api/auth/login/` → returns `access` and `refresh` tokens
- Refresh: POST `/api/auth/refresh/` (payload: `refresh`)

Jobs:
- List / Create: `GET|POST /api/jobs`
- Detail / Update / Delete: `GET|PATCH|DELETE /api/jobs/<id>/`

Applications:
- Apply: `POST /api/applications/` (payload: `job`, `cover_letter`)
- Update status (employer): `PATCH /api/applications/<id>/status/` (payload: `status`)

All protected endpoints require the header: `Authorization: Bearer <ACCESS_TOKEN>`

## ERD
A draft ERD has been added at `docs/ERD.md` (Mermaid diagram + notes).

## Tests & Manual QA
Manual cURL tests were executed for:
- User registration and login
- Creating a job as an employer
- Applying as a job seeker
- Accepting an application as the employer

Automated tests and CI are pending (recommended next step).

## Remaining / Next steps
- Add ERD visual export (PNG/SVG) and presentation materials
- Integrate Swagger/OpenAPI docs (`/api/docs`)
- Add automated tests and GitHub Actions CI
- Deploy to a hosting provider (Render / Railway / Heroku)
- Add job categories, search/filtering, and performance optimizations

---

If you want, I can add Swagger docs, generate a PNG for the ERD, or create automated tests next. ✅
