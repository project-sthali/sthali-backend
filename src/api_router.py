from typing import Dict, List
from fastapi import APIRouter as FAPIRouter
from uuid import UUID
from pydantic import BaseModel


from .crud import create, delete, read, read_all, update, upsert
from .exceptions import APIException
from .schemas import Schemas


class Routes:
    def __init__(self,
                 router: APIRouter,
                #  schemas: Schemas,
                #  routes: list = ['create', 'delete', 'read', 'read_all',
                #                  'update', 'upsert'],
                 ) -> None:
        self.router = router
        # self.schemas = schemas


    # def create_routes(self):

        # if 'read' in self.routes:
        #     _, schema_response = self.schemas.read

        #     @self.router.get('/{resource_id}/', response_model=schema_response)
        #     async def resource_get(resource_id: UUID) -> Dict:
        #         try:
        #             resource_obj = await read(resource_id)
        #             return resource_obj
        #         except Exception as e:
        #             raise APIException(
        #                 detail=e.detail,
        #                 status_code=e.status_code)

        # if 'create' in self.routes:
        #     schema_payload, schema_response = self.schemas.create

        #     @self.router.post('/', response_model=schema_response)
        #     async def resource_create(
        #             resource_payload: schema_payload) -> Dict:
        #         try:
        #             resource_obj = await create(resource_payload)
        #             return resource_obj
        #         except Exception as e:
        #             raise APIException(
        #                 detail=e.detail,
        #                 status_code=e.status_code)

        # if 'update' in self.routes:
        #     schema_payload, schema_response = self.schemas.update

        #     @self.router.put('/{resource_id}/', response_model=schema_response)
        #     async def resource_update(
        #             resource_id: UUID,
        #             resource_payload: schema_payload) -> Dict:
        #         try:
        #             resource_obj = await update(resource_id, resource_payload)
        #             return resource_obj
        #         except Exception as e:
        #             raise APIException(
        #                 detail=e.detail,
        #                 status_code=e.status_code)

        # if 'upsert' in self.routes:
        #     schema_payload, schema_response = self.schemas.upsert

        #     @self.router.patch('/{resource_id}/',
        #                        response_model=schema_response)
        #     async def resource_upsert(
        #             resource_id: UUID,
        #             resource_payload: schema_payload) -> Dict:
        #         try:
        #             resource_obj = await upsert(resource_id, resource_payload)
        #             return resource_obj
        #         except Exception as e:
        #             raise APIException(
        #                 detail=e.detail,
        #                 status_code=e.status_code)

        # if 'delete' in self.routes:
        #     _, schema_response = self.schemas.delete

        #     @self.router.delete('/{resource_id}/',
        #                         response_model=schema_response)
        #     async def resource_delete(
        #             resource_id: UUID) -> Dict:
        #         try:
        #             resource_obj = await delete(resource_id)
        #             return resource_obj
        #         except Exception as e:
        #             raise APIException(
        #                 detail=e.detail,
        #                 status_code=e.status_code)

        # return self.router



class ResourcePayload(BaseModel):
    name: str


class APIRouter:
    def __init__(self, resource_payload: ResourcePayload) -> None:
        router = FAPIRouter(prefix=f"/{resource_payload.name}", tags=[resource_payload.name])
        # schemas = Schemas(name=resource)
        # super().__init__(router, schemas)
        super().__init__(router)
