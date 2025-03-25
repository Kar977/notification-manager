from fastapi import FastAPI
from notification_manager.routers.notifications import router


app = FastAPI()


def register_routers():
    app.include_router(router)


register_routers()
