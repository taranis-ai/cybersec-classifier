from cybersec_classifier.config import Config
from cybersec_classifier.predictor import Predictor


class PredictorFactory:
    """
    Factory class that dynamically instantiates and returns the correct Predictor
    based on the configuration. This approach ensures that only the configured model
    is loaded at startup.
    """

    def __new__(cls, *args, **kwargs) -> Predictor:
        if Config.MODEL == "bart_mnli":
            from cybersec_classifier.bart_mnli import BartMNLIClassifier

            return BartMNLIClassifier(*args, **kwargs)
        if Config.MODEL == "mlp":
            from cybersec_classifier.cybersec_mlp import MLPClassifier

            return MLPClassifier(*args, **kwargs)

        raise ValueError(f"Unsupported model: {Config.MODEL}")
