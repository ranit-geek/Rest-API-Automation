from jsonschema import validate


def validate_schema(json_schema, response):
    result = validate(response,json_schema)





