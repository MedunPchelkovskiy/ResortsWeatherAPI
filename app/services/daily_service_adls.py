import io

import pyarrow.parquet as pq
from azure.identity import ClientSecretCredential
from azure.storage.filedatalake import DataLakeServiceClient

from app.core.config import settings


def _get_adls_client() -> DataLakeServiceClient:
    credential = ClientSecretCredential(
        tenant_id=settings.tenant_id,
        client_id=settings.client_id,
        client_secret=settings.client_secret,
    )
    return DataLakeServiceClient(
        account_url=settings.account_url,
        credential=credential,
    )


def _latest_parquet_path() -> str:
    """Finds the path to the most recent hour.parquet file."""
    client = _get_adls_client()
    fs = client.get_file_system_client("rawdata")

    base = "MyLakehouse/Meteo/gold/five-day-forecast"

    # List all paths and find the latest by name (lexicographic = chronological)
    paths = [p.name for p in fs.get_paths(path=base, recursive=True)
             if p.name.endswith(".parquet")]

    if not paths:
        raise FileNotFoundError("No parquet files found in Data Lake.")

    return max(paths)  # latest by path string sort


def get_latest_forecast(resort_name: str) -> list[dict]:
    """
    Reads the latest parquet file from ADLS and filters by place_name.
    Returns list of dicts ready for Pydantic serialization.
    """
    client = _get_adls_client()
    fs = client.get_file_system_client("rawdata")

    path = _latest_parquet_path()
    file_client = fs.get_file_client(path)

    download = file_client.download_file()
    data = download.readall()

    table = pq.read_table(io.BytesIO(data))
    df = table.to_pandas()

    filtered = df[df["place_name"] == resort_name].head(5)
    return filtered.to_dict(orient="records")
