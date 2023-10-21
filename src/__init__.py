from sthali_crud import FieldDefinition, ResourceSpecification, SthaliCRUD
from .db import DB


_resource_spec = ResourceSpecification(
    name='people',
    fields=[
        FieldDefinition(
            name='name',
            type=str,
        ),
        # FieldDefinition(
        #     name='height',
        #     type=int,
        #     has_default=True,
        #     default_value=123,
        #     allow_none=True,
        # ),
        FieldDefinition(
            name='age',
            type=int,
        ),
    ]
)


_db: DB = DB()
_sthalicrud: SthaliCRUD = SthaliCRUD(resource_spec=_resource_spec, db=_db)
# _sthalicrud.replace_models(_sthalicrud.schema)

fastapi = _sthalicrud.app
