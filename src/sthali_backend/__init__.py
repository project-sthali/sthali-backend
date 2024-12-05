"""This module provides ..."""

import pydantic

import sthali_crud

from .config import Config

__all__ = [
    "AppSpecification",
    "Config",
    "SthaliBackend",
    "default_lifespan",
]


default_lifespan = sthali_crud.default_lifespan


@pydantic.dataclasses.dataclass(kw_only=True)
class AppSpecification(sthali_crud.AppSpecification):
    """Represents the specification of a SthaliBackend application."""

    def __post_init__(self):
        self.title = "SthaliBackend"
        self.description = "A FastAPI package for implement services."

class SthaliBackend(sthali_crud.SthaliCRUD):
    def __init__(self, app_spec: AppSpecification) -> None:
        super().__init__(app_spec)
