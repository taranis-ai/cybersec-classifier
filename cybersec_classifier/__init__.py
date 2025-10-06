from flask import Flask
from cybersec_classifier import router


def create_app():
    app = Flask(__name__)
    app.config.from_object("cybersec_classifier.config.Config")

    router.init(app)
    return app


def init(app: Flask):
    router.init(app)


if __name__ == "__main__":
    create_app().run()
