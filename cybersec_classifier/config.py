from functools import lru_cache
from typing import Literal
from taranis_base_bot.protocols import Predictor
from taranis_base_bot.config import CommonSettings


class Settings(CommonSettings):
    MODEL: Literal["mlp", "bart_mnli"] = "mlp"


Config = Settings()


@lru_cache(maxsize=1)
def get_model() -> Predictor:
    if Config.MODEL == "mlp":
        from cybersec_classifier.cybersec_mlp import MLPClassifier

        return MLPClassifier()
    elif Config.MODEL == "bart_mnli":
        from cybersec_classifier.bart_mnli import BartMNLIClassifier

        return BartMNLIClassifier()
    else:
        raise ValueError(f"Unknown model {Config.MODEL!r}")
