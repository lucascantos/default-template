from dataclasses import InitVar, dataclass
from src.helpers.objects import ParamsSchema


@dataclass
class PathParams:
    params: InitVar[ParamsSchema]

    def __post_init__(self, params):
        self.query_params = params.query_params
        self.path_params = params.path_params

    @property
    def serverless(self):
        return {
            "paths": {key: True for key in self.path_params},
            "querystrings": {key: True for key in self.query_params},
        }

    @property
    def swagger(self):

        from copy import deepcopy

        def _convert_to_openapi(key, value, type):
            # Helper function to convert

            meta = value.pop("meta", {})
            value.pop("coerce", None)
            value.pop("nullable", None)

            value["name"] = key
            value["in"] = type
            value["schema"] = {
                "type": value.pop("type"),
                "enum": value.pop("allowed", None),
                "example": meta.get("example", None),
            }

            # Remove empty variables from schema
            for k, v in value["schema"].copy().items():
                if not v:
                    value["schema"].pop(k)

            return value

        params = []
        qp = deepcopy(self.query_params)
        for k, v in qp.items():
            param = _convert_to_openapi(k, v, "query")
            params.append(param)

        pp = deepcopy(self.path_params)
        for k, v in pp.items():
            param = _convert_to_openapi(k, v, "path")
            params.append(param)

        return params
