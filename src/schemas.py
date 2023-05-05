from uuid import UUID
from pydantic import BaseModel, create_model


class FieldName(BaseModel):
    required: bool = True


class SchemaFields(BaseModel):
    name: FieldName


class SchemaDefinition(BaseModel):
    fields: SchemaFields


class Schemas:
    def __init__(self, name: str) -> None:
        self.read = (None, f"{name.title()}ResponseSchema")
        self.create = (f"{name.title()}CreateSchema", f"{name.title()}CreateResponseSchema")
        self.update = (f"{name.title()}UpdateSchema", f"{name.title()}UpdateResponseSchema")
        self.upsert = (f"{name.title()}UpsertSchema", f"{name.title()}UpsertResponseSchema")
        self.delete = (None, f"{name.title()}DeleteResponseSchema")




# class BaseSchema(BaseModel):
#     id: UUID


# class MockResource(BaseSchema):
#     name: str = 'ResourceResponseSchema'
#     fields: dict = {'name': {'required': True}}


# schema = {
#     'ResourceResponseSchema': {
#         'fields': {
#             'name': {
#                 'required': True
#             }
#         }
#     }
# }


# def create_schemas(schema: MockResource):
#     fields = {field_name: (str, (None, ...)[field_attr['required']])
#               for field_name, field_attr
#               in schema.fields.items()}
#     return create_model(schema.name,
#                         __base__=BaseSchema,
#                         **fields)
