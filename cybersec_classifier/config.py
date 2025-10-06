from functools import lru_cache
from typing import Literal
from taranis_base_bot.protocols import Predictor
from taranis_base_bot.config import get_settings as get_common_settings
from cybersec_classifier.cybersec_mlp import MLPClassifier
from cybersec_classifier.bart_mnli import BartMNLIClassifier

Config = get_common_settings()
MODEL: Literal["mlp", "bart_mnli"] = "mlp"


@lru_cache(maxsize=1)
def get_model() -> Predictor:
    if MODEL == "mlp":
        return MLPClassifier()
    if MODEL == "bart_mnli":
        return BartMNLIClassifier()
    raise ValueError(f"Unknown model {MODEL!r}")
