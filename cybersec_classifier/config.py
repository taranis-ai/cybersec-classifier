from typing import Literal
from taranis_base_bot.config import CommonSettings


class Settings(CommonSettings):
    MODEL: Literal["cybersec_mlp", "bart_mnli"] = "cybersec_mlp"
    PACKAGE_NAME: str = "cybersec_classifier"
    HF_MODEL_INFO: bool = True
    PAYLOAD_KEY: str = "text"


Config = Settings()
