"""
Integration test for GET /resorts.

This hits your actual local PostgreSQL instance (via DATABASE_URL in .env),
so it assumes `gold_yearly` already has rows for your 3 resorts. Run it
once you've pointed the app at your local DB:

    pytest app/tests/test_resorts.py -v
"""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_get_resorts_returns_list() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/resorts")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    # Expect your 3 ski resorts once gold_yearly is populated locally.
    if body:
        assert "resort_name" in body[0]
