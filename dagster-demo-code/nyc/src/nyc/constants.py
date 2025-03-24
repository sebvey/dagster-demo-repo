from dataclasses import dataclass
import os
from pathlib import Path

# PRJ PATHS
NYC_PATH = Path(os.getenv("NYC_PATH"))
RAW_PATH = NYC_PATH / "raw"

# PRJ GLOBAL CONSTANTS
START_DATE: str = "2023-01-01"
END_DATE: str = "2024-01-01"

# RAW TAXI TRIPS
TAXI_TRIPS_RAW_PATH = RAW_PATH / "taxi_trips"
TAXI_TRIPS_FILE_TEMPLATE = "taxi_trips_{}.parquet"

# RAW TAXI ZONES
TAXI_ZONES_RAW_PATH = RAW_PATH / "taxi_zones"
TAXI_ZONES_FILENAME = "taxi_zones.csv"


@dataclass
class PrjGroup:
    Raw = "raw"
    Warehouse = "warehouse"
