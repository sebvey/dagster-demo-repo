import dagster as dg
import dagster_duckdb as dgd

from ._taxi_zones_raw import taxi_zones_raw
from ..constants import PrjGroup, TAXI_ZONES_RAW_PATH, TAXI_ZONES_FILENAME


@dg.asset(
    deps=[taxi_zones_raw],
    group_name=PrjGroup.Warehouse,
)
def taxi_zones_table(db: dgd.DuckDBResource) -> None:
    "Taxi zones loaded in the zones duckdb table."

    query = f"""
        create or replace table zones as (
            select
                LocationID as zone_id,
                zone,
                borough,
                the_geom as geometry
            from '{str(TAXI_ZONES_RAW_PATH / TAXI_ZONES_FILENAME)}'
        );
    """

    with db.get_connection() as conn:
        conn.execute(query)
