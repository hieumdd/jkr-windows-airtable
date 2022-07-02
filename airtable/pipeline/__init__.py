from airtable.pipeline import sout_sales_calendar

pipelines = {
    i.name: i
    for i in [
        j.pipeline  # type: ignore
        for j in [
            sout_sales_calendar,
        ]
    ]
}
