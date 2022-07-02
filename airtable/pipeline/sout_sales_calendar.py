from airtable.pipeline import interface, utils

pipeline = interface.Pipeline(
    name="SoutSalesCalendar",
    table_id="soutsalescalendarjkr%40gmail.com",
    transform=lambda rows: [
        {
            "title": row.get("Title"),
            "status_color": [i for i in row["Status-Color"]]
            if row.get("Status-Color")
            else [],
            "date": utils.parse_timestamp(row.get("Date")),
            "end": utils.parse_timestamp(row.get("End")),
            "number_of_windows": row.get("# Of Windows"),
            "number_of_doors": row.get("# Of Doors"),
            "director_name": row.get("Director Name"),
            "coordinator_name": row.get("Coordinator Name"),
            "value_contract_total": row.get("$ Contract Total"),
            "creator": row.get("Creator"),
            "status": row.get("Status"),
            "location": row.get("Location"),
            "description": row.get("Description"),
            "attendees": row.get("Attendees"),
            "created": utils.parse_timestamp(row.get("Created")),
            "updated": utils.parse_timestamp(row.get("Updated")),
            "event_id": row.get("Event ID"),
            "sync_source": row.get("Sync Source"),
            "all_day": row.get("All Day"),
            "start": utils.parse_timestamp(row.get("Start")),
            "event_link": row.get("Event Link"),
            "hangouts_link": row.get("Hangouts Link"),
        }
        for row in rows
    ],
    schema=[
        {"name": "title", "type": "STRING"},
        {"name": "status_color", "type": "STRING", "mode": "REPEATED"},
        {"name": "date", "type": "TIMESTAMP"},
        {"name": "end", "type": "TIMESTAMP"},
        {"name": "number_of_windows", "type": "NUMERIC"},
        {"name": "number_of_doors", "type": "NUMERIC"},
        {"name": "director_name", "type": "STRING"},
        {"name": "coordinator_name", "type": "STRING"},
        {"name": "value_contract_total", "type": "NUMERIC"},
        {"name": "creator", "type": "STRING"},
        {"name": "status", "type": "STRING"},
        {"name": "location", "type": "STRING"},
        {"name": "description", "type": "STRING"},
        {"name": "attendees", "type": "STRING"},
        {"name": "created", "type": "TIMESTAMP"},
        {"name": "updated", "type": "TIMESTAMP"},
        {"name": "event_id", "type": "STRING"},
        {"name": "sync_source", "type": "STRING"},
        {"name": "all_day", "type": "BOOLEAN"},
        {"name": "start", "type": "TIMESTAMP"},
        {"name": "event_link", "type": "STRING"},
        {"name": "hangouts_link", "type": "STRING"},
    ],
)
