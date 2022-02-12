from src.helpers.logger import log
from src.helpers.response import make_response
from src.helpers.validator import validate
from src.schemas.api_params import send_hello
from src.services.sentry import init_sentry_sdk

init_sentry_sdk()


def hello(event: dict = None, context: dict = None) -> dict:
    # Default route
    log.info(event)

    # Validate inputs
    coerced_document, errors = validate(event, send_hello.aws_event)
    if errors:
        return make_response(errors, 400)

    return make_response("Success!")

