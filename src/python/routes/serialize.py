# src/python/routes/serialize.py

# PASO 4: Insecure Deserialization
# CODIGO SEGURO
import json
import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)
router = APIRouter()

class UserPreferences(BaseModel):
    theme: str
    language: str
    notifications: bool

@router.post("/load-prefs")
async def load_prefs(data: str):
    try:
        raw = json.loads(data)
        validated = UserPreferences(**raw)
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        raise HTTPException(status_code=400, detail="JSON inválido")
    except ValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail="Datos inválidos")

    return validated.model_dump()
