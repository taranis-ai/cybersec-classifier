from taranis_base_bot.blueprint import create_service_blueprint
from taranis_base_bot.modelinfo import provider_for
from cybersec_classifier.config import get_model_instance
from taranis_base_bot.decorators import api_key_required


def init(app):
    app.url_map.strict_slashes = False
    model = get_model_instance()

    def request_parser(data: dict) -> dict:
        text = data.get("text", "")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("No text provided for cybersecurity classification")
        return {"text": text}

    bp = create_service_blueprint(
        name="bot",
        url_prefix="/",
        predict_fn=model.predict,
        modelinfo_provider=provider_for(model),
        request_parser=request_parser,
        method_decorators=[api_key_required],
    )
    app.register_blueprint(bp)
