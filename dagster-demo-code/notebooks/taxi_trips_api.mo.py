import marimo

__generated_with = "0.11.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    from pathlib import Path
    return Path, mo, pl


@app.cell
def _(Path):
    file_path = Path("/Users/ippon/code/prj-roots/dagster-demo/nyc_taxi/taxi_trips_api") / "taxi_trips_2023-12.parquet"
    return (file_path,)


@app.cell
def _(file_path, pl):
    df_schema = pl.read_parquet_schema(file_path)
    return (df_schema,)


@app.cell
def _(df_schema):
    df_schema
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
