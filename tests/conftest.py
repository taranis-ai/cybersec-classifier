import pytest

from cybersec_classifier.bart_mnli import BartMnli
from cybersec_classifier.cybersec_mlp import CybersecMlp


@pytest.fixture(scope="session")
def cybersec_mlp():
    yield CybersecMlp()


@pytest.fixture(scope="session")
def bart_mnli():
    yield BartMnli()
