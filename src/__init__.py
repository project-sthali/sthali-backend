from fastapi import FastAPI

from .libs.sthali_crud import SthaliCRUD, ResourceSpec, Field


resource_spec = ResourceSpec(
    name='people',
    fields=[
        Field(
            name='id',
            type=int,
            required=True,
        ),
        Field(
            name='name',
            type=str,
            required=True,
        ),
        Field(
            name='height',
            type=int,
            required=False,
            default=123,
        ),
    ]
)


fastapi = FastAPI()
SthaliCRUD(fastapi, resource_spec)
