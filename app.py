from cybersec_classifier.config import Config
from taranis_base_bot import create_default_bot_app

app = create_default_bot_app(Config.PACKAGE_NAME, Config)
