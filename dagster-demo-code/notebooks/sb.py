import marimo

__generated_with = "0.11.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import duckdb
    import polars
    import altair as alt
    return alt, duckdb, mo, os, polars


@app.cell
def _(duckdb, os):
    DB_PATH = os.getenv("NYC_DATABASE")
    duckdb_conn = duckdb.connect(DB_PATH)
    return DB_PATH, duckdb_conn


@app.cell
def _(duckdb_conn, manhattan_stats, mo):
    _df = mo.sql(
        f"""
        select count(*) from manhattan_stats
        """,
        engine=duckdb_conn
    )
    return


@app.cell(disabled=True)
def _(alt, manhattan_stats, mo):
    chart = alt.Chart(manhattan_stats).mark_line().encode(x="pickup_date",y="trip_distance_sum")
    mo.ui.altair_chart(chart)
    return (chart,)


@app.cell
def _(duckdb_conn, mo, trips):
    _df = mo.sql(
        f"""
        with

        s1 as (
            select
                partition_date,
                strftime(dropoff_datetime, '%Y-%m') as drop_month,
                strftime(pickup_datetime, '%Y-%m') as pickup_month
            from trips
        ),

        s2 as (
            select
                *,
                case
                    when drop_month != partition_date or pickup_month != partition_date then 1
                    else 0
                end as not_compliant
            from s1
        )

        select
            partition_date,
            count(*) as row_count,
            sum(not_compliant) as not_compliant,
        from s2
        group by partition_date
        order by partition_date
        """,
        engine=duckdb_conn
    )
    return


@app.cell
def _():
    create_query = """
        create table manhattan_stats (
            pickup_date date,
            borough varchar,
            trip_distance_sum float,
            trip_distance_mean float,
            amount_total float,
            amount_mean float
        )
    """
    return (create_query,)


@app.cell
def _(create_query, duckdb):
    duckdb.query(create_query)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
