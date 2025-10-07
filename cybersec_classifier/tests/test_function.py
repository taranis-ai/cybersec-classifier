from cybersec_classifier.bart_mnli import BartMNLIClassifier
from cybersec_classifier.cybersec_mlp import MLPClassifier


def test_request_parser_error(client):
    response = client.post("/", json={"another_key": ""})
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "No text provided for cybersecurity classification"


def test_cybersec_classification_bart_mnli(bart_mnli: BartMNLIClassifier):
    result = bart_mnli.predict("This is a general text about flowers.")
    assert isinstance(result, dict)
    assert set(result.keys()) == {"cybersecurity", "non-cybersecurity"}
    assert result["cybersecurity"] < result["non-cybersecurity"]

    result = bart_mnli.predict("The newest development in malware automation are concerning")
    assert result["cybersecurity"] > result["non-cybersecurity"]


def test_cybersec_classification_mlp(mlp: MLPClassifier):
    result = mlp.predict("This is a general text about flowers.")
    assert isinstance(result, dict)
    assert set(result.keys()) == {"cybersecurity", "non-cybersecurity"}
    assert result["cybersecurity"] < result["non-cybersecurity"]

    result = mlp.predict("The newest development in malware automation are concerning")
    assert result["cybersecurity"] > result["non-cybersecurity"]
