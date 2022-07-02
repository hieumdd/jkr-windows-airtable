from typing import Any, Callable

from dataclasses import dataclass


@dataclass
class Pipeline:
    name: str
    table_id: str
    transform: Callable[[list[dict[str, Any]]], list[dict[str, Any]]]
    schema: list[dict[str, Any]]
