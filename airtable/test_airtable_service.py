import pytest

from airtable.airtable_service import pipeline_service
from airtable.pipeline import pipelines


@pytest.mark.parametrize(
    "pipeline",
    pipelines.values(),
    ids=pipelines.keys(),
)
def test_service(pipeline):
    res = pipeline_service(pipeline)
    assert res["output_rows"] > 0
