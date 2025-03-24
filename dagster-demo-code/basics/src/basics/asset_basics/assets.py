import dagster as dg
import random
import polars as pl


@dg.asset(group_name="referential", description="referential asset")
def asset_referential() -> None:
    pass


@dg.asset(
    group_name="bronze",
    code_version="v0",
)
def asset_bronze() -> pl.DataFrame:
    """- code versionné
    - produit un DataFrame, géré par l'I/O DuckDB"""
    return pl.DataFrame(
        {
            "group": ["a", "a", "a", "a", "a", "b", "b", "b", "b", "b"],
            "value": [-1.1, 2.2, -3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 0.0],
        }
    )


@dg.asset(
    group_name="silver",
    automation_condition=dg.AutomationCondition.eager(),
)
def asset_silver(context: dg.AssetExecutionContext, asset_bronze: pl.DataFrame) -> pl.DataFrame:
    "lit depuis l'I/O, transforme, retourne un DataFrame"
    context.log.info("Computing 'asset_silver' ...")

    return asset_bronze.group_by("group").agg(
        pl.sum("value").alias("group_sum"),
        pl.mean("value").alias("group_mean"),
    )


@dg.asset(group_name="gold", description="gold AB", deps=[asset_silver])
def asset_gold_A() -> None:
    pass


@dg.asset(group_name="gold", description="gold asset A", deps=[asset_silver, asset_referential])
def asset_gold_B() -> dg.MaterializeResult:
    return dg.MaterializeResult(metadata={"some_indicator": random.randint(5, 10)})
