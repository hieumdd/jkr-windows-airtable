from typing import Any

from airtable.airtable_service import pipeline_service, tasks_service
from airtable.pipeline import pipelines


def airtable_controller(body: dict[str, Any]):
    if "table" in body:
        return pipeline_service(pipelines[body["table"]])
    elif "tasks" in body:
        return tasks_service()
    else:
        return {}
