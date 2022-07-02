from typing import Any

from airtable.airtable_controller import airtable_controller


def main(request) -> dict[str, Any]:
    body: dict[str, Any] = request.get_json()

    print(body)

    result = airtable_controller(body)

    print(result)

    return result
