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
    db_path = os.getenv("BASICS_RSC_DB")
    duckdb_conn = duckdb.connect(db_path)
    return db_path, duckdb_conn


@app.cell
def _(duckdb_conn, mo, src):
    _df = mo.sql(
        f"""
        select * from src
        """,
        engine=duckdb_conn
    )
    return


if __name__ == "__main__":
    app.run()
