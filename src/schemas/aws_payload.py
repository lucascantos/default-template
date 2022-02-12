import json


def event_schema(query_params: dict = {}, path_params: dict = {}) -> dict:
    # Makes as event schema for aws
    return {
        "queryStringParameters": {"type": "dict", "nullable": not bool(query_params), "schema": query_params},
        "pathParameters": {"type": "dict", "nullable": not bool(path_params), "schema": path_params},
        "body": {"type": "dict", "nullable": True, "coerce": lambda x: json.loads(x)},
    }
