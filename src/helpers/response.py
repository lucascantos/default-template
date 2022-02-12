import json


def make_response(body: dict, status_code: int = 200, sort: bool = False, metadata: dict = None) -> dict:
    """
    Make a simple response object for the API requests.
    :params body: dict, object containg the content of the response
    :params status_code: int, HTTP Status Code of the response.
    :params sort: bool, Sort the parameters with asceding order
    :params metadata: dict, Adds metadata object at the end of the file
    """
    headers = {"Access-Control-Allow-Origin": "*"}
    if sort:
        # Keeping METADATA as the last element
        body = dict(sorted(body.items(), key=lambda x: x[0]))
        if metadata is not None:
            body["meta"] = dict(sorted(metadata.items(), key=lambda x: x[0]))
    return {"statusCode": status_code, "body": json.dumps(body), "headers": headers}
