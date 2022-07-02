from typing import Any
from compose import compose

from db import bigquery
from tasks import cloud_tasks

from airtable import airtable_repo
from airtable.pipeline import interface, pipelines


def pipeline_service(pipeline: interface.Pipeline) -> dict[str, Any]:
    return compose(
        lambda x: {
            "table": pipeline.name,
            "output_rows": x,
        },
        bigquery.load(pipeline.name, pipeline.schema),
        pipeline.transform,
    )(airtable_repo.get(pipeline.table_id))


def tasks_service() -> dict[str, Any]:
    return {
        "tasks": cloud_tasks.create_tasks(
            [{"table": table} for table in pipelines.keys()],
            lambda x: x["table"],
        )
    }
