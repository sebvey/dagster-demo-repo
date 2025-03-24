import dagster as dg
import polars as pl

from .assets import asset_bronze


@dg.asset_check(
    asset=asset_bronze,
    blocking=True,
)
def src_asset_values_positive(asset_bronze: pl.DataFrame) -> dg.AssetCheckResult:
    "Checks that all values are positive"

    failing_df = asset_bronze.filter(pl.col("value") < 0)
    passed = len(failing_df) == 0

    
    return dg.AssetCheckResult(passed=passed, metadata={"failed_rows": failing_df.to_dicts()})
