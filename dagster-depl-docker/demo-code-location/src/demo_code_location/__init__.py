import dagster as dg
from datetime import datetime

daily_partitions_def = dg.DailyPartitionsDefinition(datetime(2024,1,1),datetime(2024,2,1))

@dg.asset(
    partitions_def=daily_partitions_def,
)
def asset_A(context: dg.AssetExecutionContext) -> None:
    context.log.info(f"Materializing {context.partition_key}")


defs = dg.Definitions(
    assets=[asset_A]
)
