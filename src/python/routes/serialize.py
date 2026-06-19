# src/python/routes/serialize.py

# PASO 4: Insecure Deserialization
# CÓDIGO SEGURO — usar JSON con esquema validado en lugar de pickle

import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError

router = APIRouter()


class UserPreferences(BaseModel):
    theme: str
    language: str
    notifications: bool


async def load_prefs(data: str):
    try:
        raw = json.loads(data)
        validated = UserPreferences(**raw)
-   except (json.JSONDecodeError, ValidationError) as e:  # ← eliminó la variable 'e'
+   except (json.JSONDecodeError, ValidationError):
        raise HTTPException(status_code=400, detail="Datos invalidos")

    return validated.model_dump()
