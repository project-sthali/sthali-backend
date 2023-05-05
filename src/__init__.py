from fastapi import FastAPI

from .config import CONFIG, config_app
from .api_router import Router


app = FastAPI()

config_app(app, CONFIG.cors)

for resource in ['customer', 'contact']:
    router_obj = Router(resource)
    # app.include_router(router_obj.create_routes())
