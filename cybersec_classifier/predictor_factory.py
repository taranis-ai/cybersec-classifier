from cybersec_classifier.config import Config
from cybersec_classifier.predictor import Predictor


class PredictorFactory:
    """
    Factory class that dynamically instantiates and returns the correct Predictor
    based on the configuration. This approach ensures that only the configured model
    is loaded at startup.
    """

    def __new__(cls, *args, **kwargs) -> Predictor:
        if Config.MODEL == 'bart_mnli':
            from cybersec_classifier.bart_mnli import BartMnli
            return BartMnli(*args, **kwargs)

        raise ValueError(f"Unsupported model: {Config.MODEL}")

