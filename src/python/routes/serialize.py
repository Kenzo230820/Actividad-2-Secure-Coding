# SEGURO — SafeLoader deserializa solo tipos basicos
import yaml

@router.post("/config")
async def load_config(data: str):
    config = yaml.safe_load(data)  # solo dict, list, str, int, float, bool
    return config
