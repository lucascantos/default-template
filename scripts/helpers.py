import yaml
from src.configs.general import DOMAIN


def clear_null_values(object: dict) -> dict:
    """
    Clear null values from dictionaries recursively
    :params object: dict, any dict
    """
    if isinstance(object, list):
        return [clear_null_values(entry) for entry in object if entry is not None]
    if isinstance(object, dict):
        results = {}
        for k, v in object.items():
            value = clear_null_values(v)
            if v is not None and v != {}:
                results[k] = value
        return results
    return object


def save_yaml(schema: dict, filepath: str, sort: bool = False):
    """
    Save Yaml file
    :params schema:dict file to be converted to yaml
    :params filepath:, str file path and name to save the data
    :params sort: bool, True if want sorting
    """
    with open(filepath, "w") as file:
        yaml.dump(schema, file, sort_keys=sort)


def load_yaml(filepath) -> dict:
    """
    Load Yaml file
    :params filepath:, str file path and name to load the data
    """
    with open(filepath) as file:
        return yaml.safe_load(file)


def get_openapi(paths: dict) -> dict:
    """
    Creates an OpenAPI object
    :params paths: dict, Object containing the paths of the api
    """
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Product Name",
            "description": "My_Description",
            "version": "1.0.0",
            "contact": {
                "name": "Lucas Cantos",
                "url": "https://github.com/lucascantos",
            },
        },
        "servers": [
            {"url": "https://dev-mydomain.com", "description": "Development server"},
            {"url": "https://mydomain.com", "description": "Production server"},
        ],
        "tags": [{"name": "Products", "description": ""}],
        "paths": paths,
    }
