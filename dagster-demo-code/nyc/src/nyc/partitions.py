import dagster as dg

from . import constants  as cst


monthly_partition = dg.MonthlyPartitionsDefinition(
    start_date=cst.START_DATE,
    end_date=cst.END_DATE,
)

weekly_partition = dg.WeeklyPartitionsDefinition(
    start_date=cst.START_DATE,
    end_date=cst.END_DATE,
)
