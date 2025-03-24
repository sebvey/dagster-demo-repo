import dagster as dg
import polars as pl
import os
from pathlib import Path

from .. import constants as cst
from ._taxi_trips_raw import taxi_trip_raw

expected_schema = {
    "VendorID": pl.Int32,
    "tpep_pickup_datetime": pl.Datetime(time_unit="ns", time_zone=None),
    "tpep_dropoff_datetime": pl.Datetime(time_unit="ns", time_zone=None),
    "passenger_count": pl.Int64,
    "trip_distance": pl.Float64,
    "RatecodeID": pl.Int64,
    "store_and_fwd_flag": pl.String,
    "PULocationID": pl.Int32,
    "DOLocationID": pl.Int32,
    "payment_type": pl.Int64,
    "fare_amount": pl.Float64,
    "extra": pl.Float64,
    "mta_tax": pl.Float64,
    "tip_amount": pl.Float64,
    "tolls_amount": pl.Float64,
    "improvement_surcharge": pl.Float64,
    "total_amount": pl.Float64,
    "congestion_surcharge": pl.Float64,
    "Airport_fee": pl.Float64,
}


@dg.asset_check(
    asset=taxi_trip_raw,
    blocking=False,
)
def taxi_trip_api_schema_compliant(context: dg.AssetCheckExecutionContext) -> dg.AssetCheckResult:
    "Checks that all taxi trip api parquet files have compliant schema"

    files_path: Path = cst.TAXI_TRIPS_RAW_PATH

    problematic_files = []

    for entry in os.scandir(files_path):
        if entry.is_file():
            actual_schema = pl.read_parquet_schema(entry.path)
            if actual_schema != expected_schema:
                problematic_files.append(entry.name)
    problematic_files.sort()

    return dg.AssetCheckResult(
        passed=len(problematic_files) == 0,
        severity=dg.AssetCheckSeverity.WARN,
        metadata={"problematic_files": problematic_files},
    )
