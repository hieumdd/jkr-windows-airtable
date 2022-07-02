from typing import Optional

import dateparser


def parse_timestamp(value: Optional[str]):
    if not value:
        return None
    else:
        try:
            timestamp = dateparser.parse(value)
            return timestamp.isoformat("seconds") if timestamp else None
        except:
            return None
