from scripts.objects import PathParams
from scripts.helpers import clear_null_values
from scripts.helpers import get_openapi
from scripts.helpers import load_yaml, save_yaml
from src.schemas.api_params import schemas


def update_serverless() -> dict:
    """
    Updates serverless yml file by adding the parameters required.
    Returns an object with the API paths for the swagger file
    TODO:   Right now, Cerberus is the root for the schema. 
            Ideally this should not be a more universal format
    """
    sls_filepath = "serverless.yml"
    sls_data = load_yaml(sls_filepath)
    swagger_paths = {}

    # Go through fuctions
    for func_name, func_properties in sls_data["functions"].items():
        # Go through events
        for event in func_properties["events"]:
            # Skip non http events
            if not event.get("http"):
                continue

            event["cors"] = {"origin": "*", "headers": "${self:custom.corsAllowedHeaders}"}
            # get validation schema
            schema = schemas.get(func_name.replace("-", "_"))
            if schema:
                path_params = PathParams(schema)
                # For Serverless
                event["request"] = {"parameters": path_params.serverless}

                # For Swagger
                description = event.get("description")
                path = event["http"]["path"]
                method = event["http"]["method"]
                swagger_paths[f"/{path}"] = {
                    method: {
                        "tags": ["Products"],
                        "operationId": func_name,
                        "description": description,
                        "parameters": path_params.swagger,
                        "responses": {"200": {"description": "200 response"}},
                    }
                }
    swagger_paths = clear_null_values(swagger_paths)
    sls_data = clear_null_values(sls_data)

    save_yaml(sls_data, sls_filepath)
    return swagger_paths


if __name__ == "__main__":
    swagger_paths = update_serverless()
    openapi_file = get_openapi(swagger_paths)
    save_yaml(openapi_file, "docs/swagger.yml")
