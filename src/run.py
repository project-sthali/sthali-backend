import os

from spec_example import EXAMPLE_SPEC
from sthali_backend import AppSpecification, SthaliBackend, load_and_parse_spec_file, APIKeyAuth, APIKey


api_key = APIKey("api_key")
api_key_auth = APIKeyAuth(api_key, "header", "service")


dependencies = [api_key_auth.dependency]
spec_file_path = os.getenv("SPEC_FILE_PATH")
app_spec_dict = load_and_parse_spec_file(spec_file_path) if spec_file_path else EXAMPLE_SPEC
client = SthaliBackend(AppSpecification(**app_spec_dict, dependencies=dependencies))
app = client.app
