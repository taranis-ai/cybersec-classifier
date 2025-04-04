from cybersec_classifier.predictor import Predictor
from transformers import pipeline


class BartMNLIClassifier(Predictor):
    model_name = "facebook/bart-large-mnli"
    candidate_labels = ["cybersecurity", "non-cybersecurity"]

    def __init__(self):
        self.model = pipeline("zero-shot-classification", model=self.model_name)

    def predict(self, text: str) -> dict:
        classification_result = self.model(text, self.candidate_labels, multi_label=True)
        predicted_labels = classification_result.get("labels", [])
        scores = classification_result.get("scores", [])
        if not scores or not predicted_labels:
            raise ValueError(f"Failed to classify text: {text}")
        return dict(zip(predicted_labels, scores))
