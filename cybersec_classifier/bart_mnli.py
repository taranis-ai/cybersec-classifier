from cybersec_classifier.predictor import Predictor
from transformers import pipeline
from cybersec_classifier.log import logger


class BartMNLIClassifier(Predictor):
    model_name = "facebook/bart-large-mnli"
    candidate_labels = ["security", "non-security"]

    def __init__(self):
        self.model = pipeline("zero-shot-classification", model=self.model_name)

    def predict(self, text: str) -> dict:
        classification_result = self.model(text, self.candidate_labels)
        scores = classification_result.get("scores", None)
        if not scores or not isinstance(scores, list):
            logger.error("Classifier did not produce valid classification scores")
            scores = [0.0, 0.0]

        return dict(zip(self.candidate_labels, scores))
