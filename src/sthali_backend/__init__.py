from sthali_auth import APIKey, APIKeyAuth
from sthali_crud import AppSpecification, SthaliCRUD, load_and_parse_spec_file


class SthaliBackend:
    def __init__(self, app_spec: AppSpecification) -> None:
        sthali_crud = SthaliCRUD(app_spec)
        self.app = sthali_crud.app


__all__ = [
    "APIKey",
    "APIKeyAuth",
    "AppSpecification",
    "load_and_parse_spec_file",
    "SthaliBackend",
]
