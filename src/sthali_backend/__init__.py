from sthali_auth import http_basic, credentials, security
from sthali_crud import AppSpecification, SthaliCRUD, load_and_parse_spec_file


class SthaliBackend:
    def __init__(self, app_spec: AppSpecification) -> None:
        self.app = SthaliCRUD(app_spec)


__all__ = [
    "AppSpecification",
    "SthaliBackend",
    "load_and_parse_spec_file",
    "http_basic",
    "credentials",
    "security",
]
