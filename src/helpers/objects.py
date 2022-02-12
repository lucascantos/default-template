from dataclasses import dataclass, field, InitVar
import json
from src.helpers.logger import log


@dataclass
class ParamsSchema:
    query_params: dict = field(default_factory=dict, repr=False)
    path_params: dict = field(default_factory=dict, repr=False)

    @property
    def aws_event(self):
        return {
            "queryStringParameters": {
                "type": "dict",
                "nullable": not bool(self.query_params),
                "schema": self.query_params,
            },
            "pathParameters": {"type": "dict", "nullable": not bool(self.path_params), "schema": self.path_params},
            "body": {"type": "dict", "nullable": True, "coerce": lambda x: json.loads(x)},
        }