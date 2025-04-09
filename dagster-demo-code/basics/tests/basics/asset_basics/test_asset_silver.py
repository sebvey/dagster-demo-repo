import dagster as dg
import polars as pl
import pytest


from basics.asset_basics.assets import asset_silver

# On test la fonction qui porte la transformation de manière classique
# Ici on mock le contexte du run (utilisé uniquement pour logger dans la transfo)

bronze_1_schema = pl.Schema({"group": pl.String, "value": pl.Float32})
bronze_2_schema = pl.Schema({"group": pl.String, "desc": pl.String})
silver_schema = pl.Schema(
    {
        "group": pl.String,
        "bronze_1_sum": pl.Float32,
        "bronze_1_mean": pl.Float32,
        "desc": pl.String,
    }
)


@pytest.fixture
def context() -> dg.AssetExecutionContext:
    return dg.build_asset_context()


def test_asset_silver_schema(context: dg.AssetExecutionContext) -> None:
    input_1 = pl.DataFrame(schema=bronze_1_schema)
    input_2 = pl.DataFrame(schema=bronze_2_schema)

    output = asset_silver(context=context, asset_bronze_1=input_1, asset_bronze_2=input_2)
    assert output.schema == silver_schema


def test_asset_silver_transfo(context: dg.AssetExecutionContext) -> None:
    input_1 = pl.DataFrame(
        {
            "group": ["a", "a", "b", "b"],
            "value": [1.0, 2.0, 3.0, 4.0],
        }
    )

    input_2 = pl.DataFrame({"group": ["a", "b"], "desc": ["Alpha group", "Beta group"]})

    expected = pl.DataFrame(
        {
            "group": ["a", "b"],
            "bronze_1_sum": [3.0, 7.0],
            "bronze_1_mean": [1.5, 3.5],
            "desc": ["Alpha group", "Beta group"],
        }
    )

    actual = asset_silver(context=context, asset_bronze_1=input_1, asset_bronze_2=input_2)

    assert expected.equals(actual)
