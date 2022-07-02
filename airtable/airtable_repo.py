from typing import Optional, Any
import os

import httpx

AIRTABLE_BASE_ID = "appeWBLilrekl3IXq"


def get_client():
    return httpx.Client(
        base_url=f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}",
        headers={"Authorization": f"Bearer {os.getenv('AIRTABLE_API_KEY')}"},
    )


def get(table: str):
    def _get(
        client: httpx.Client,
        offset: Optional[str] = None,
    ) -> list[dict[str, Any]]:
        r = client.get(
            f"/{table}",
            params={"offset": offset},
        )
        r.raise_for_status()
        res = r.json()

        records = [i["fields"] for i in res["records"]]
        offset = res.get("offset")

        return records if not offset else records + _get(client, offset)

    with get_client() as client:
        return _get(client)
