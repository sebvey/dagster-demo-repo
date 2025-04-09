import dagster as dg
import polars as pl

from .assets import asset_bronze_1


@dg.asset_check(
    asset=asset_bronze_1,
    blocking=True,
)
def src_asset_values_positive(asset_bronze: pl.DataFrame) -> dg.AssetCheckResult:
    "Checks that all values are positive"

    failing_rows = asset_bronze.filter(pl.col("value") < 0)
    passed = len(failing_rows) == 0

    return dg.AssetCheckResult(passed=passed, metadata={"failed_rows": failing_rows.to_dicts()})
