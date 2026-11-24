import os
from pydantic_settings import BaseSettings, SettingsConfigDict

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE_PATH = os.path.join(CURRENT_DIR, ".env")

class Settings(BaseSettings):
    user: str
    key: str
    url: str = "http://hub.browserstack.com/wd/hub"
    timeout: float = 20.0

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH)

settings = Settings()
