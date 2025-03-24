import marimo

__generated_with = "0.11.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import duckdb
    return duckdb, mo, os


@app.cell
def _(duckdb, os):
    DB_PATH = os.getenv("NYC_DATABASE")
    duckdb_conn = duckdb.connect(DB_PATH)
    return DB_PATH, duckdb_conn


@app.cell
def _(duckdb_conn, mo, trips):
    _df = mo.sql(
        f"""
        select * from trips limit 10
        """,
        engine=duckdb_conn
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
