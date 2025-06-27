from fastapi import FastAPI

from core.config import settings
from contextlib import asynccontextmanager
from core.models import db_helper, Base
from router.api_v1 import user_router, client_router, order_router, note_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield





app = FastAPI(lifespan=lifespan)

app.include_router(router=user_router)
app.include_router(router=client_router)
app.include_router(router=order_router)
app.include_router(router=note_router)