import dagster as dg
import dagster_duckdb as dgduck

from . import assets

all_assets = dg.load_assets_from_modules([assets])
all_asset_checks = dg.load_asset_checks_from_modules([assets])

db_resource = dgduck.DuckDBResource(database=dg.EnvVar("NYC_DATABASE"))

resources = {"db": db_resource}

defs = dg.Definitions(
    assets=all_assets,
    asset_checks=all_asset_checks,
    resources= resources,
)
