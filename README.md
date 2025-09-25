# Tesla Sensor Tool
A FastAPI-based API to evaluate vehicle sensor safety (speed vs. distance). Built to demonstrate backend skills for Tesla's Full Stack Developer role.

## Features
- Accepts lists of speeds and distances via query params.
- Returns safety verdicts (safe/danger) for each pair.
- CORS-enabled for frontend integration.

## Setup
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
