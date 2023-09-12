from dataclasses import field
from typing import Any, Callable, Dict, List, Literal, Optional, Union, Tuple
from uuid import UUID

from pydantic.dataclasses import dataclass

from .crud import create, read, read_all, update, upsert, delete


@dataclass
class Route:
    """Route
    """
    path: str
    endpoint: Callable[..., Any]
    response_model: Any
    methods: List[Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE']]
    # name: str
    # params: Dict[str, tuple[type, Any]] = field(default_factory=dict)
    # description: str = ''
    # status_code: int = 200
    # response_description: str = ''


@dataclass
class Resource:
    """Resource
    """
    @staticmethod
    def default_routes() -> List[Route]:
        """Generate basic CRUD routes

        Returns:
            List[Route]: List of default CRUD operations
        """
        return [
            Route(
                path='/',
                endpoint=create,
                response_model=dict,
                methods=['POST'],
            ),
            Route(
                path='/{resource_id}/',
                endpoint=read,
                response_model=dict,
                methods=['GET'],
            ),
            Route(
                path='/',
                endpoint=read_all,
                response_model=List[dict],
                methods=['GET'],
            ),
            Route(
                path='/',
                endpoint=update,
                response_model={},
                methods=['PATCH'],
            ),
            Route(
                path='/{resource_id}/',
                endpoint=upsert,
                response_model={},
                methods=['PUT'],
            ),
            Route(
                path='/{resource_id}/',
                endpoint=delete,
                response_model=None,
                methods=['DELETE'],
            )
        ]

    prefix: str
    tags: List[str]
    routes: List[Route] = field(default_factory=default_routes)


resources = [
    Resource(
        prefix='/batata',
        tags=['batata']
    ),
    # # Resource(
    # #     prefix='/cenoura',
    # #     tags=['cenoura'],
    # #     routes=[
    # #         Route(
    # #             path='/',
    # #             endpoint=get_all_resources,
    # #             response_model=dict,
    # #             methods=['GET'],
    # #             # name='get all resources',
    # #         ),
    # #         Route(
    # #             path='/',
    # #             endpoint=get_resource,
    # #             response_model=dict,
    # #             methods=['GET'],
    # #             # name='get resource',
    # #         )

    #     ]
    # ),



    # Resource(
    #     prefix='/teste',
    #     tags=['teste'],
    #     routes=[
    #         Route(
    #             path='/',
    #             endpoint=Callable,
    #             response_model=str,
    #             methods=['GET'],
    #             name='get resource',
    #         ),
    #         Route(
    #             path='/{resource_id}/',
    #             endpoint=Callable,
    #             response_model=List[str],
    #             methods=['GET'],
    #             name='get resource',
    #             params={'resource_id': (str, 'me'), 'fields': (str, None)},
    #             # description='get resource',
    #             # status_code=200,
    #             # response_description='response_description',
    #         ),
    #         # Route(
    #         #     path='/',
    #         #     response_model=List[Dict],
    #         #     name='create resource',
    #         #     method='POST',
    #         # ),
    #         # Route(
    #         #     response_model=List[Dict],
    #         #     path='/',
    #         #     method='PUT',
    #         # ),
    #         # Route(
    #         #     response_model=List[Dict],
    #         #     path='/',
    #         #     method='PATCH',
    #         # ),
    #         # Route(
    #         #     response_model=List[Dict],
    #         #     path='/',
    #         #     method='DELETE',
    #         # ),
    #     ]
    # )
]
