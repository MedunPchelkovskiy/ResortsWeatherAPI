from datetime import date, datetime

from pydantic import BaseModel


class DailyOut(BaseModel):
    """
    Response schema for one day of weather data.

    Note there's no separate "request schema" here — GET requests don't
    carry a JSON body in REST conventions, so there's nothing for Pydantic
    to validate as a body model. The "request validation" for this endpoint
    happens through the path parameter (ResortName enum) and the query
    parameters (typed + constrained directly in the route function below).
    Pydantic body schemas like this one matter for POST/PUT, where the
    client sends JSON you need to validate.
    """

    forecast_date_utc: date
    place_name: str | None

    temp_min: float | None
    temp_max: float | None
    temp_avg: float | None

    rain_min: float | None
    rain_max: float | None
    rain_avg: float | None

    snow_min: float | None
    snow_max: float | None
    snow_avg: float | None

    wind_speed_min: float | None
    wind_speed_max: float | None
    wind_speed_avg: float | None

    cloud_cover_min: float | None
    cloud_cover_max: float | None
    cloud_cover_avg: float | None

    humidity_min: float | None
    humidity_max: float | None
    humidity_avg: float | None

    generated_at: datetime

    model_config = {"from_attributes": True}