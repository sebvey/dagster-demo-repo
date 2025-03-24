import dagster as dg
import dagster_duckdb as dgd
from ..constants import PrjGroup
from ._taxi_trips_table import taxi_trips_table
from ..partitions import monthly_partition
from ._taxi_zones_table import taxi_zones_table


create_query = """
    create table if not exists manhattan_stats (
        pickup_yearmonth varchar,
        pickup_date date,
        borough varchar,
        trip_distance_sum float,
        trip_distance_mean float,
        amount_total float,
        amount_mean float
    )
"""


def query_string(yearmonth: str) -> str:
    return f"""
        delete from manhattan_stats where pickup_yearmonth = '{yearmonth}';
        insert into manhattan_stats
        with
        filtered as (
            select
                *,
                cast(pickup_datetime as date) as pickup_date,
                strftime(pickup_datetime, '%Y-%m') as pickup_yearmonth
            from trips
            where partition_date = '{yearmonth}' and pickup_yearmonth = '{yearmonth}'
        ),

        joined as (
            select
                filtered.*,
                zones.zone,
                zones.borough,
            from filtered
            inner join zones on zones.zone_id = filtered.pickup_zone_id
            where zones.borough = 'Manhattan'
        )

        select
            pickup_yearmonth,
            pickup_date,
            borough,
            sum(trip_distance) as trip_distance_sum,
            mean(trip_distance) as trip_distance_mean,
            sum(total_amount) as amount_total,
            mean(total_amount) as amount_mean
        from joined
        group by pickup_yearmonth, pickup_date, borough
        order by pickup_date
    """


@dg.asset(
    deps=[taxi_trips_table, taxi_zones_table],
    partitions_def=monthly_partition,
    group_name=PrjGroup.Warehouse,
)
def manhattan_stats(context: dg.AssetExecutionContext, db: dgd.DuckDBResource) -> None:

    yearmonth = context.partition_key[:-3]

    context.log.info(f"materizaling {yearmonth}")
    with db.get_connection() as conn:
        conn.execute(create_query)
        context.log.info("CREATE QUERY DONE")

        conn.execute(query_string(yearmonth))
