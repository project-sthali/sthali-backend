"""This module provides ..."""
from contextlib import asynccontextmanager
from logging import info
from typing import Annotated

from fastapi import FastAPI
from pydantic import Field
from pydantic.dataclasses import dataclass

from sthali_auth import APIKey, APIKeyAuth
from sthali_crud import AppSpecification as CRUDAppSpecification
from sthali_crud import ResourceSpecification as CRUDResourceSpecification
from sthali_crud import SthaliCRUD, load_and_parse_spec_file


@dataclass
class ResourceSpecification(CRUDResourceSpecification):
    """Represents the specification of the resource.

    Attributes:
        db (DBSpecification): The database specification for the resource.
        name (str): The name of the resource.
        fields (list[FieldDefinition]): The list of field definitions for the resource.
    """
    auth: None


@dataclass
class AppSpecification(CRUDAppSpecification):
    """Represents the specification of a SthaliBackend application.

    Attributes:
        service (ServiceSpecification): {...}.
        crud (CRUDAppSpecification): Represents the specification of a SthaliCRUD application.
    """
    resources: Annotated[
        list[ResourceSpecification], Field(default_factory=list, description="The list of resource specifications")
    ]

    # dependencies: Annotated[list, Field(default=None, description="The dependencies for the application")]
    # description: Annotated[
    #     str, Field(default="A FastAPI package for CRUD operations", description="The description of the application")
    # ]
    # summary: Annotated[str | None, Field(default=None, description="The summary of the application")]
    # title: Annotated[str, Field(default="SthaliCRUD", description="The title of the application")]
    # version: Annotated[str, Field(default="0.1.0", description="The version of the application")]

    # service: Annotated[ServiceSpecification, Field(description="...")]
    # crud: CRUDAppSpecification


@asynccontextmanager
async def default_lifespan(app: FastAPI):
    """A context manager that handles the startup and shutdown of SthaliBackend.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None
    """
    info("Startup SthaliBackend")
    yield
    info("Shutdown SthaliBackend")


class SthaliBackend(SthaliCRUD):
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
