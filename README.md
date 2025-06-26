python -m venv .venv

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

command to run env
.\.venv\Scripts\Activate.ps1

pip install fastapi uvicorn

uvicorn main:app --reload

pip install pydantic[email]
pip install psycopg2 reverse_geocoder