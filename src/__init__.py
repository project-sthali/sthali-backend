from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI
from pydantic import create_model

# from .config import CONFIG, config_app
from .types import resources


app = FastAPI()
# config_app(app, CONFIG.cors)


for resource in resources:
    prefix = resource.prefix
    tags = resource.tags
    router = APIRouter(
        prefix=prefix,
        tags=tags
    )
    for route in resource.routes:
        print(route)
        path = route.path
        endpoint = route.endpoint
        response_model = route.response_model
        methods = route.methods
        # name = route.name
        # dependencies = [Depends(create_model('params', **route.params))]

        router.add_api_route(path=path, endpoint=endpoint,
                             response_model=response_model, methods=methods)

        # @router.api_route(path=path, response_model=response_model, methods=methods, name=name)
        # async def call(params_model: create_model('params', **params) = Depends()):
        #     return {}
        #     return {params_model}

    app.include_router(router)
