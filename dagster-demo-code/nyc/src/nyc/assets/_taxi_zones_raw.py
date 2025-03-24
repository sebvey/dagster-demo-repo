import requests
import dagster as dg

from ..constants import PrjGroup, TAXI_ZONES_RAW_PATH, TAXI_ZONES_FILENAME


@dg.asset(
    group_name=PrjGroup.Raw,
)
def taxi_zones_raw() -> None:
    "Raw CSV file for the taxi zones dataset. Sourced from the NYC Open Data portal."

    response = requests.get(
        "https://community-engineering-artifacts.s3.us-west-2.amazonaws.com/dagster-university/data/taxi_zones.csv"
    )

    if not response.status_code == 200:
        raise Exception(f"Bad response. Got code {response.status_code}")

    TAXI_ZONES_RAW_PATH.mkdir(parents=True, exist_ok=True)
    with open(TAXI_ZONES_RAW_PATH / TAXI_ZONES_FILENAME, "wb") as output_file:
        output_file.write(response.content)
