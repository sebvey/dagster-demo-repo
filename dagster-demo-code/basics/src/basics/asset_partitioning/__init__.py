import dagster as dg
from datetime import datetime

monthly_partitions_def = dg.MonthlyPartitionsDefinition(
    start_date=datetime(2024, 1, 1), end_date=datetime(2024, 7, 1)
)

static_partitions_def = dg.StaticPartitionsDefinition(["X", "Y"])

partitions_def = dg.MultiPartitionsDefinition(
    {"month": monthly_partitions_def, "static": static_partitions_def}
)


@dg.asset(partitions_def=partitions_def)
def asset_partitioned_A(context: dg.AssetExecutionContext) -> None:

    context.log.info(f"Materializing {context.partition_key}")
    context.log.info(f"{context.partition_key.keys_by_dimension=}")


@dg.asset(partitions_def=partitions_def, deps=[asset_partitioned_A])
def asset_partitioned_B() -> None:
    pass


defs = dg.Definitions(assets=[asset_partitioned_A, asset_partitioned_B])
