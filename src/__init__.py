from sthali_crud import Field, SthaliCRUD, ResourceSpec
from .db import DB

_resource_spec = ResourceSpec(
    name='people',
    fields=[
        # Field(
        #     name='id',
        #     type=int,
        # ),
        Field(
            name='name',
            type=str,
        ),
        Field(
            name='height',
            type=int,
            default=123,
            allow_none=False,
        ),
    ]
)

_db = DB()
_sthalicrud = SthaliCRUD(_resource_spec=_resource_spec, _db=_db)
DB.replace_model(_sthalicrud.model)

fastapi = _sthalicrud.app
