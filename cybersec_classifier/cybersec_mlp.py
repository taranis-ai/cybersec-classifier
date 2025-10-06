from sentence_transformers import SentenceTransformer
from huggingface_hub import hf_hub_download
import joblib


class MLPClassifier:
    """
    Classifier based on embed + MLP
    URL: https://huggingface.co/selfconstruct3d/cybersec_classifier

    """

    model_name = "selfconstruct3d/cybersec_classifier"
    candidate_labels = ["non-cybersecurity", "cybersecurity"]

    def __init__(self) -> None:
        model_path = hf_hub_download(repo_id=self.model_name, filename="cybersec_classifier.pkl")
        self.model = joblib.load(model_path)
        self.embedder = SentenceTransformer("intfloat/multilingual-e5-large")

    def predict(self, text: str, **_: object) -> dict[str, float]:
        embedding = self.embedder.encode([text], convert_to_numpy=True, show_progress_bar=False)
        if scores := self.model.predict_proba(embedding).tolist()[0]:
            return dict(zip(self.candidate_labels, scores))
        else:
            raise ValueError(f"Failed to classify text: {text}")
