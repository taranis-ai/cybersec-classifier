from cybersec_classifier.bart_mnli import BartMnli
from cybersec_classifier.cybersec_mlp import CybersecMlp


import pytest


@pytest.mark.asyncio
async def test_cybersec_classification_bart_mnli(bart_mnli: BartMnli):
    result = await bart_mnli.predict("This is a general text about flowers.")
    assert isinstance(result, dict)
    assert set(result.keys()) == {"cybersecurity", "non-cybersecurity"}
    assert result["cybersecurity"] < result["non-cybersecurity"]

    result = await bart_mnli.predict("The newest development in malware automation are concerning")
    assert result["cybersecurity"] > result["non-cybersecurity"]


@pytest.mark.asyncio
async def test_cybersec_classification_cybersec_mlp(cybersec_mlp: CybersecMlp):
    result = await cybersec_mlp.predict("This is a general text about flowers.")
    assert isinstance(result, dict)
    assert set(result.keys()) == {"cybersecurity", "non-cybersecurity"}
    assert result["cybersecurity"] < result["non-cybersecurity"]

    result = await cybersec_mlp.predict("The newest development in malware automation are concerning")
    assert result["cybersecurity"] > result["non-cybersecurity"]
