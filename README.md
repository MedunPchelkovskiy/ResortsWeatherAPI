# Resort Weather API

Read-only FastAPI service that serves aggregated weather data from the
existing gold-layer tables (bronze → silver → gold_daily → ... → gold_seasonal)
produced by the separate Prefect pipeline. This service does **not** own the
schema and does **not** run migrations — it only reads.

## Structure

```
app/
├── main.py             # FastAPI app + router registration
├── core/
│   └── config.py       # Settings (DATABASE_URL etc.) from env / .env
├── db/
│   ├── base.py         # SQLAlchemy declarative base
│   └── session.py      # Async engine, session factory, get_db dependency
├── models/
│   └── gold.py         # ORM models mirroring existing gold tables (read-only)
├── schemas/
│   └── resort.py        # Pydantic response models
├── routers/
│   └── resorts.py       # GET /resorts
├── services/
│   └── resort_service.py # Query logic (kept separate from the route handler)
└── tests/
    ├── test_health.py
    └── test_resorts.py
```

## ⚠️ Schema assumption — adjust before running

`app/models/gold.py` defines `GoldYearly` with a guessed set of columns
(`resort_name`, `year`, `avg_temp_c`, `total_snow_days`, `total_precip_mm`).
Only `resort_name` is actually required for `GET /resorts`. Update the
column list (names + types) to match your real `gold_yearly` table before
running against your database — otherwise SQLAlchemy will raise on columns
that don't exist.

If you'd rather start from `gold_seasonal` or another gold table for the
`/resorts` query, just point `resort_service.list_resorts` at that model
instead — any gold table with a `resort_name` column works equally well for
a distinct-names list.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # then edit DATABASE_URL
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for Swagger UI.

## Tests

```bash
pytest -v
```

`test_health.py` needs no DB. `test_resorts.py` hits your real local
Postgres through the actual app, so it expects `gold_yearly` to already
have rows for your resorts.

## Next steps (per your roadmap)

1. Adjust `GoldYearly` columns to your real schema, confirm `GET /resorts`
   returns your 3 resorts locally.
2. Add the next endpoint(s): `GET /resorts/{place_name}/yearly`,
   `.../season`, `.../forecast` — each gets its own model (if a new gold
   table is involved), schema, and a function in a resort-scoped service
   module.
3. Dockerize (`Dockerfile` + `docker-compose.yml` for local Postgres).
4. Deploy with your existing Terraform/CI-CD setup.

Resist adding `repositories/`, `middleware/`, or extra DI layers until an
endpoint actually needs them — same principle as the pipeline project: start
simple, extract when needed.
