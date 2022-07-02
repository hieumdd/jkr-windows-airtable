import json

import pytest

from airtable import airtable_repo
from airtable.pipeline import pipelines


@pytest.mark.parametrize(
    "pipeline",
    pipelines.values(),
    ids=pipelines.keys(),
)
def test_get(pipeline):
    data = airtable_repo.get(pipeline.table_id)
    with open("test.json", "w") as f:
        json.dump(data, f)

    assert data
