from flask import Flask, Blueprint, jsonify, request
from flask.views import MethodView

from cybersec_classifier.predictor import Predictor
from cybersec_classifier.predictor_factory import PredictorFactory
from cybersec_classifier.decorators import api_key_required, debug_request


class BotEndpoint(MethodView):
    def __init__(self, bot: Predictor) -> None:
        super().__init__()
        self.bot = bot

    @debug_request
    @api_key_required
    def post(self):
        data = request.get_json()
        text = data.get("text", "")

        classification_result = self.bot.predict(text)
        return jsonify(classification_result)


class HealthCheck(MethodView):
    @debug_request
    def get(self):
        return jsonify({"status": "ok"})


class ModelInfo(MethodView):
    def __init__(self, bot: Predictor):
        super().__init__()
        self.bot = bot

    @debug_request
    def get(self):
        return jsonify(self.bot.modelinfo)


def init(app: Flask):
    bot = PredictorFactory()
    app.url_map.strict_slashes = False
    bot_bp = Blueprint("bot", __name__)
    bot_bp.add_url_rule("/", view_func=BotEndpoint.as_view("predict", bot=bot))
    bot_bp.add_url_rule("/health", view_func=HealthCheck.as_view("health"))
    bot_bp.add_url_rule("/modelinfo", view_func=ModelInfo.as_view("modelinfo", bot=bot))
    app.register_blueprint(bot_bp)
