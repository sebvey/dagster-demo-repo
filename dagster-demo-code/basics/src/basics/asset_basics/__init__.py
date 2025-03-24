import dagster as dg
from dagster_duckdb_polars import DuckDBPolarsIOManager


from . import assets, asset_checks
from .asset_jobs import gold_AB_job, gold_AR_job

# MODULE DEFINITION

# Dagster Definitions type -> what is loaded by dagster
# no matter the name.
# only one object of type Definitions at root namespace of the module

location_assets = dg.load_assets_from_modules([assets])
location_asset_checks = dg.load_asset_checks_from_modules([asset_checks])
location_jobs = [gold_AR_job,gold_AB_job]


defs = dg.Definitions(
    assets=location_assets,
    asset_checks=location_asset_checks,
    jobs=location_jobs,
    resources={
        "io_manager": DuckDBPolarsIOManager(database=dg.EnvVar("BASICS_IO_DB"), schema="basics_io")
    },
)
