import dagster as dg

from .assets import asset_referential, asset_bronze_1, asset_silver, asset_gold_A, asset_gold_B


selection_job = dg.define_asset_job(
    name="selection_job",
    selection=[asset_referential, asset_bronze_1, asset_silver, asset_gold_A],
    description="all assets in a selection",
)


upstream_job = dg.define_asset_job(
    name="upstream_job",
    selection=dg.AssetSelection.assets(asset_gold_B).upstream(),
    description="asset_gold_B and all upstream dependencies",
)


# Asset selection: Many ways to define it
# - list of python objects
# - selection from names, with upstream / downstream syntax
# ...
# https://docs.dagster.io/guides/build/assets/asset-selection-syntax
