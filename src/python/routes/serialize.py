# src/python/routes/serialize.py

# PASO 4: Insecure Deserialization
# CÓDIGO SEGURO — usar JSON con esquema validado en lugar de deserialización insegura

from fastapi import APIRouter
from pydantic import BaseModel, Field, ConfigDict

router = APIRouter()


class ConfigPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nombre: str = Field(..., min_length=1, max_length=100)
    entorno: str = Field(..., min_length=1, max_length=50)
    activo: bool
    version: int = Field(..., ge=1)


@router.post("/config")
async def load_config(config: ConfigPayload):
    return {
        "nombre": config.nombre,
        "entorno": config.entorno,
        "activo": config.activo,
        "version": config.version
    }
