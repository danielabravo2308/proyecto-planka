import pytest
import jsonschema


class AssertionSchemas:


    @staticmethod
    def validate_list_output_schema(list , schema_output):
        try:
            jsonschema.validate(instance=list, schema= schema_output)
        except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")
    


    @staticmethod
    def validate_schema_input_payload(payload , schema_input):
        try:
            jsonschema.validate(instance=payload, schema= schema_input)
        except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")


    @staticmethod
    def validate_schema_output_payload(response , schema_output):
        try:
            jsonschema.validate(instance=response.json(), schema= schema_output)
        except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")


    