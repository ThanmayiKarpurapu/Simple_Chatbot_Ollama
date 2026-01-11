import yaml
from pathlib import Path
from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    name: str
    provider: str
    temperature: float
    max_tokens: int

class Config(BaseModel):
    model: ModelConfig

def load_config(config_path="config.yaml"):
    with open(config_path) as f:
        data = yaml.safe_load(f)
    return Config(**data)
