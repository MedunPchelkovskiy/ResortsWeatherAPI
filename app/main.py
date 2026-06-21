from fastapi import FastAPI

from app.routers import resorts

app = FastAPI(
    title="Resort Weather API",
    description="Read-only API serving aggregated weather data from the gold layer of the resort weather pipeline.",
    version="0.1.0",
)

app.include_router(resorts.router)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
