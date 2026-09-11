from fastapi import FastAPI

from ai_commerce_mind.api.router import api_router
from ai_commerce_mind.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.app_debug,
    )
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()
