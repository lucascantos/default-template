from cerberus import Validator


def validate(document: dict, schema: dict) -> tuple:
    """
    Checks if the document is following the schema rules
    :params document: dict, Object to be validated
    :params schema: dict, Object with rules
    return tuple, Coerced document, Erros found
    """
    v = Validator(schema)
    v.allow_unknown = True
    v.validate(document)
    return v.document, v.errors
