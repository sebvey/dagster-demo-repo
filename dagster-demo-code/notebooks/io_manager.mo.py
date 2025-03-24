import marimo

__generated_with = "0.11.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import duckdb
    import polars as pl
    import os
    return duckdb, mo, os, pl


@app.cell
def _(duckdb, os):
    # /!\ permanent connection - you should shut down notebook properly
    db_path = os.getenv("BASICS_IO_DB")
    duckdb_conn = duckdb.connect(db_path)
    return db_path, duckdb_conn


@app.cell
def _(basics_io, duckdb_conn, mo, src_asset):
    _df = mo.sql(
        f"""
        select * from basics_io.src_asset
        """,
        engine=duckdb_conn
    )
    return


@app.cell
def _(basics_io, duckdb_conn, mo, tgt_asset):
    _df = mo.sql(
        f"""
        select * from basics_io.tgt_asset
        """,
        engine=duckdb_conn
    )
    return


@app.cell
def _(pl):
    pl.DataFrame(
            {
                "id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                "group": ["a", "a", "a", "a", "a", "b", "b", "b", "b", "b"],
                "value": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 0.0],
            }).schema
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
