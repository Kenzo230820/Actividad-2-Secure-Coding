# CODIGO SEGURO
import json
import yaml
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError

router = APIRouter()

class UserPreferences(BaseModel):
    theme: str
    language: str
    notifications: bool

@router.post("/config")
async def load_config(data: str):
    config = yaml.safe_load(data)  # solo dict, list, str, int, float, bool
    return config
