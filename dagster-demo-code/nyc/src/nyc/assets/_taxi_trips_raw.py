import requests
import dagster as dg

from ..partitions import monthly_partition
from ..constants import PrjGroup, TAXI_TRIPS_FILE_TEMPLATE, TAXI_TRIPS_RAW_PATH


@dg.asset(
        partitions_def=monthly_partition,
        group_name=PrjGroup.Raw,
    )
def taxi_trip_raw(context: dg.AssetExecutionContext) -> None:
    "The raw parquet files for the taxi trips dataset. Sourced from the NYC Open Data Portal."

    # Monthly Partitioning - we get first day of month from the context
    context.log.info(f"{context.partition_key=}")

    partition_date_str = context.partition_key
    month_to_fetch = partition_date_str[:-3]
    raw_trips = requests.get(
        f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month_to_fetch}.parquet"
    )

    output_file_path = TAXI_TRIPS_RAW_PATH / TAXI_TRIPS_FILE_TEMPLATE.format(month_to_fetch)
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file_path, "wb") as output_file:
        output_file.write(raw_trips.content)
