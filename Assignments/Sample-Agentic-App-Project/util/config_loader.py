import yaml
from typing import Any, Dict
from pathlib import Path

def load_config(config_path: str = "config/app_config.yaml") -> Dict[str, Any]:
    """
    Loads a YAML configuration file and returns its contents as a dictionary.
    Raises FileNotFoundError or yaml.YAMLError if issues occur.
    """
    config_file = Path(config_path)
    if not config_file.is_file():
        raise FileNotFoundError(f"Configuration file not found: {config_file.resolve()}")
    try:
        with config_file.open("r") as file:
            return yaml.safe_load(file) or {}
    except yaml.YAMLError as e:
        raise RuntimeError(f"Error parsing YAML file: {e}")


class ConfigLoader:
    def __init__(self):
        print(f"Loaded config.....")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]