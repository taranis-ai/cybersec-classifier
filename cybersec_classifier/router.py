from taranis_base_bot.blueprint import create_service_blueprint
from taranis_base_bot.modelinfo import get_hf_modelinfo
from taranis_base_bot.decorators import api_key_required
from cybersec_classifier.config import get_model


def request_parser(data: dict) -> dict:
    text = data.get("text", "")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("No text provided for cybersecurity classification")
    return {"text": text}


def init(app):
    app.url_map.strict_slashes = False
    model = get_model()

    model_name = getattr(model, "model_name", None)
    modelinfo_fn = (lambda: get_hf_modelinfo(model_name)) if isinstance(model_name, str) else (lambda: {"model": "unknown"})

    bp = create_service_blueprint(
        name="bot",
        url_prefix="/",
        predict_fn=model.predict,
        modelinfo_fn=modelinfo_fn,
        request_parser=request_parser,
        method_decorators=[api_key_required],
    )
    app.register_blueprint(bp)
