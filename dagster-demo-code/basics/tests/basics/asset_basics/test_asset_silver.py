import dagster as dg
import polars as pl
import pytest


from basics.asset_basics.assets import asset_silver

# On test la fonction qui porte la transformation de manière classique
# Ici on mock le contexte du run (utilisé uniquement pour logger dans la transfo)

bronze_schema = pl.Schema({"group": pl.String, "value": pl.Float32})
silver_schema = pl.Schema({"group": pl.String, "group_sum": pl.Float32, "group_mean": pl.Float32})


@pytest.fixture
def context() -> dg.AssetExecutionContext:
    return dg.build_asset_context()


def test_asset_silver_schema(context: dg.AssetExecutionContext) -> None:
    input = pl.DataFrame(schema=bronze_schema)
    output = asset_silver(context=context, asset_bronze=input)
    assert output.schema == silver_schema


def test_asset_silver_transfo(context: dg.AssetExecutionContext) -> None:
    input = pl.DataFrame(
        {
            "group": ["a", "a", "b", "b"],
            "value": [1.0, 2.0, 3.0, 4.0],
        }
    )

    expected = pl.DataFrame(
        {
            "group": ["a", "b"],
            "group_sum": [3.0, 7.0],
            "group_mean": [1.5, 3.5],
        }
    )

    actual = asset_silver(context=context, asset_bronze=input)

    assert expected.equals(actual)
