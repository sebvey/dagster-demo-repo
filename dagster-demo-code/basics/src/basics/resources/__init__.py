import dagster as dg
from dagster_duckdb import DuckDBResource


create_request = """
create table if not exists src as
select i as 'id', i * i as 'value'
from range(0,10) as t(i);
"""

@dg.asset
def resourced_asset(duckdb: DuckDBResource) -> None:
    with duckdb.get_connection() as conn:
        conn.execute(create_request)


defs = dg.Definitions(
    assets=[resourced_asset],
    resources={
        "duckdb": DuckDBResource(database=dg.EnvVar("BASICS_RSC_DB"))  # loaded at runtime
    },
)
