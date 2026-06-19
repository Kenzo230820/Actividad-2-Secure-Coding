# src/python/routes/serialize.py

# PASO 4: Insecure Deserialization
# CÓDIGO SEGURO — usar JSON con esquema validado en lugar de deserialización insegura

import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError

router = APIRouter()


class UserPreferences(BaseModel):
    theme: str
    language: str
    notifications: bool

    class Config:
        extra = "forbid"


@router.post("/load-prefs")
async def load_prefs(data: str):
    try:
        raw = json.loads(data)
        validated = UserPreferences(**raw)
    except (json.JSONDecodeError, ValidationError):
        raise HTTPException(status_code=400, detail="Datos inválidos")

    return validated.dict()
