from flask import Flask
from cybersec_classifier import router
from cybersec_classifier.config import Config
from taranis_base_bot.log import configure_logger


def create_app():
    app = Flask(__name__)

    configure_logger(
        module=Config.MODULE_ID,
        debug=Config.DEBUG,
        colored=Config.COLORED_LOGS,
        syslog_address=None,
    )

    app.config.from_object("cybersec_classifier.config.Config")

    router.init(app)
    return app


def init(app: Flask):
    router.init(app)


if __name__ == "__main__":
    create_app().run()
