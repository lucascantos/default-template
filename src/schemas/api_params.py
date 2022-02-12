'''
This is the most work you probably have to put into.
Here we define the schema for validating the api requests
'''
from src.helpers.objects import ParamsSchema

query_schema = {}

path_schema = {}

# AWS serverless event payload schema
send_hello = ParamsSchema(query_schema, path_schema)