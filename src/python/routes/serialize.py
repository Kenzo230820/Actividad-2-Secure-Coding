# src/python/routes/serialize.py
# PASO 4: Insecure Deserialization — usar JSON con schema validado en lugar de pickle
# CODIGO SEGURO
# VULNERABLE — yaml.load() sin Loader ejecuta constructores Python
import yaml

@router.post("/config")
async def load_config(data: str):
    config = yaml.load(data)  # ejecuta codigo YAML arbitrario
    return config
!!python/object/apply:os.system
- "id > /tmp/rce.txt"

# SEGURO — SafeLoader deserializa solo tipos basicos
import yaml

@router.post("/config")
async def load_config(data: str):
    config = yaml.safe_load(data)  # solo dict, list, str, int, float, bool
    return config
