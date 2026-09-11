from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ai_commerce_mind.db.session import get_db_session

router = APIRouter()

DbSession = Annotated[AsyncSession, Depends(get_db_session)]


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready")
async def readiness(
    session: DbSession,
) -> dict[str, str]:
    await session.execute(text("SELECT 1"))

    return {
        "status": "ready",
        "database": "ok",
    }
