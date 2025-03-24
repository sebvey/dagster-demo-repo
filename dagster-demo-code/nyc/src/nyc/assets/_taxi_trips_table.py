import dagster as dg
import dagster_duckdb as dgduck

from ._taxi_trips_raw import taxi_trip_raw
from ..constants import PrjGroup, TAXI_TRIPS_FILE_TEMPLATE, TAXI_TRIPS_RAW_PATH
from ..partitions import monthly_partition


create_table_query = """
create table if not exists trips (
    vendor_id integer, pickup_zone_id integer, dropoff_zone_id integer,
    rate_code_id double, payment_type integer, dropoff_datetime timestamp,
    pickup_datetime timestamp, trip_distance double, passenger_count double,
    total_amount double, partition_date varchar
);
"""


def upsert_query(loaded_month: str) -> str:
    loaded_file = TAXI_TRIPS_RAW_PATH / TAXI_TRIPS_FILE_TEMPLATE.format(loaded_month)

    return f"""
        delete from trips where partition_date = '{loaded_month}';
        insert into trips
        select
            VendorID,
            PULocationID,
            DOLocationID,
            RatecodeID,
            payment_type,
            tpep_dropoff_datetime,
            tpep_pickup_datetime,
            trip_distance,
            passenger_count,
            total_amount,
            '{loaded_month}' as partition_date
        from '{str(loaded_file)}';
    """


@dg.asset(
    deps=[taxi_trip_raw],
    partitions_def=monthly_partition,
    group_name=PrjGroup.Warehouse,
)
def taxi_trips_table(context: dg.AssetExecutionContext, db: dgduck.DuckDBResource):
    "Raw Taxi Trip dataset, loaded into a duckDB database, partitioned by month"

    partition_date_str = context.partition_key
    loaded_month = partition_date_str[:-3]

    context.log.info(f"materizaling {partition_date_str}")

    with db.get_connection() as conn:
        context.log.info("EXECUTING CREATE TABLE QUERY")
        conn.execute(create_table_query)
        context.log.info("EXECUTING UPSERT QUERY")
        conn.execute(upsert_query(loaded_month))
