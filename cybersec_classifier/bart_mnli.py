from transformers import pipeline


class BartMNLIClassifier:
    """
    Zero-shot classifier using BART-MNLI
    Model URL: https://huggingface.co/facebook/bart-large-mnli
    """

    model_name = "facebook/bart-large-mnli"
    candidate_labels = ["non-cybersecurity", "cybersecurity"]

    def __init__(self) -> None:
        self.model = pipeline("zero-shot-classification", model=self.model_name)

    def predict(self, text: str, **_: object) -> dict:
        classification_result = self.model(text, self.candidate_labels, multi_label=True)
        predicted_labels = classification_result.get("labels", [])
        scores = classification_result.get("scores", [])
        if not scores or not predicted_labels:
            raise ValueError(f"Failed to classify text: {text}")
        return dict(zip(predicted_labels, scores))
