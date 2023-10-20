from pydantic.dataclasses import dataclass
from sthali_crud import FieldDefinition, SthaliCRUD, ResourceSpec
from .db import DB


_resource_spec = ResourceSpec(
    name='people',
    fields=[
        FieldDefinition(
            name='name',
            type=str,
        ),
        FieldDefinition(
            name='height',
            type=int,
            has_default=True,
            default_value=123,
            allow_none=True,
        ),
        FieldDefinition(
            name='age',
            type=int,
        ),
    ]
)


_db = DB()
_sthalicrud = SthaliCRUD(_resource_spec=_resource_spec, _db=_db)
# DB.replace_model(_sthalicrud.model)

fastapi = _sthalicrud.app
