from sqlalchemy import CheckConstraint, Text
from sqlalchemy import String, Integer, Date, TIMESTAMP, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class GoldYearly(Base):
    """
    Mirrors the `gold_yearly_summarized_data` table produced by the pipeline.
    """

    __tablename__ = "gold_yearly_summarized_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    place_name: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    period_start: Mapped[object] = mapped_column(Date, nullable=False)
    period_type: Mapped[str] = mapped_column(Text, nullable=False)

    generated_at: Mapped[object] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    temp_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    rain_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    snow_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    wind_speed_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    cloud_cover_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    humidity_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    __table_args__ = (
        UniqueConstraint("place_name", "year", "period_type", name="uq_place_period"),
        CheckConstraint(
            "period_type IN ('yearly', 'Q1', 'Q2', 'Q3', 'Q4', 'winter', 'spring', 'summer', 'autumn')",
            name="ck_period_type_valid"
        ),
    )


class GoldMonthly(Base):
    """
    Mirrors the `gold_monthly_summarized_data` table produced by the pipeline.
    """

    __tablename__ = "gold_monthly_summarized_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    place_name: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    month_number: Mapped[int] = mapped_column(Integer, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)

    month_start: Mapped[object] = mapped_column(Date, nullable=False)
    generated_at: Mapped[object] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )

    temp_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    rain_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    snow_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    wind_speed_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    cloud_cover_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    humidity_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "place_name",
            "year",
            "month_number",
            name="uq_place_year_month",
        ),
    )


class GoldWeekly(Base):
    """
    Mirrors the `gold_weekly_summarized_data` table.
    """

    __tablename__ = "gold_weekly_summarized_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    place_name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    week_number: Mapped[int] = mapped_column(Integer, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    week_start: Mapped[object] = mapped_column(Date, nullable=False)
    generated_at: Mapped[object] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    temp_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    rain_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    snow_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    wind_speed_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    cloud_cover_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    humidity_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    __table_args__ = (
        UniqueConstraint("place_name", "year", "week_number", name="uq_place_year_week"),
    )



class GoldFiveDayForecast(Base):
    """
    Mirrors the `gold_five_day_forecast_data` table produced by the pipeline.
    """

    __tablename__ = "gold_five_day_forecast_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    place_name: Mapped[str | None] = mapped_column(Text, nullable=True)

    ingest_date: Mapped[object | None] = mapped_column(Date, nullable=True)
    ingest_hour: Mapped[int | None] = mapped_column(Integer, nullable=True)

    forecast_date_utc: Mapped[object | None] = mapped_column(Date, nullable=True)

    generated_at: Mapped[object | None] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )

    temp_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    rain_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    snow_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    wind_speed_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    cloud_cover_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    humidity_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "place_name",
            "forecast_date_utc",
            "ingest_date",
            "ingest_hour",
            name="idx_gold_forecast_unique",
        ),
    )


class GoldDaily(Base):
    """
    Mirrors the `gold_daily_summarized_data` table produced by the pipeline.
    """

    __tablename__ = "gold_daily_summarized_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    place_name: Mapped[str] = mapped_column(Text, nullable=False, index=True)

    ingest_date: Mapped[object] = mapped_column(Date, nullable=False)
    ingest_hour: Mapped[int] = mapped_column(Integer, nullable=False)

    forecast_date_utc: Mapped[object] = mapped_column(Date, nullable=False)

    generated_at: Mapped[object] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )

    temp_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    temp_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    rain_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    rain_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    snow_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    snow_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    wind_speed_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    wind_speed_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    cloud_cover_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    cloud_cover_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    humidity_min: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_max: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    humidity_avg: Mapped[float | None] = mapped_column(Numeric, nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "place_name",
            "forecast_date_utc",
            name="unique_place_forecast_generated",
        ),
    )
