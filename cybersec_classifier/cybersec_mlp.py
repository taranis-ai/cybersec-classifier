from cybersec_classifier.predictor import Predictor
from sentence_transformers import SentenceTransformer
from huggingface_hub import hf_hub_download
import joblib


class MLPClassifier(Predictor):
    model_name = "selfconstruct3d/cybersec_classifier"
    candidate_labels = ["non-cybersecurity", "cybersecurity"]

    def __init__(self):
        model_path = hf_hub_download(repo_id=self.model_name, filename="cybersec_classifier.pkl")
        self.model = joblib.load(model_path)
        self.embedder = SentenceTransformer("intfloat/multilingual-e5-large")

    def predict(self, text: str) -> dict:
        embedding = self.embedder.encode([text], convert_to_numpy=True, show_progress_bar=False)
        if scores := self.model.predict_proba(embedding):
            return dict(zip(self.candidate_labels, scores.tolist()[0]))
        else:
            raise ValueError(f"Failed to classify text: {text}")
