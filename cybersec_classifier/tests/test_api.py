def test_root_avail(client):
    response = client.post("/", json={"text": "Health check text."})
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"status": "ok"}


def test_modelinfo_mlp(client, mlp):
    response = client.get("/modelinfo")
    assert response.status_code == 200
    data = response.get_json()
    assert data == mlp.modelinfo


def test_modelinfo_bart_mnli(client_bart_mnli, bart_mnli):
    response = client_bart_mnli.get("/modelinfo")
    assert response.status_code == 200
    data = response.get_json()
    assert data == bart_mnli.modelinfo


def test_empty_input(client):
    response = client.post("/", json={"text": ""})
    assert response.status_code == 400
    data = response.get_json()
    assert isinstance(data, dict)
    assert data["error"] == "No text provided for cybersecurity classification"


def test_invalid_json(client):
    response = client.post("/", data="notjson", content_type="application/json")
    assert response.status_code == 400


def test_valid_json_but_not_dict(client):
    """Test valid JSON that isn't a dictionary"""
    # This mimics: curl -d '"notjson"' (valid JSON string, not a dict)
    response = client.post("/", data='"notjson"', content_type="application/json")
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Wrong data format. Send payload as '{'text': 'Text to classify'}'"


def test_missing_authorization_header_with_api_key(client_with_api_key):
    """Test missing Authorization header when API key is required"""
    response = client_with_api_key.post("/", json={"text": "test"})
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "not authorized"


def test_malformed_authorization_header_syntax(client_with_api_key):
    """Test malformed Authorization header - the exact issue you encountered"""
    # This mimics: curl -H "Authorization Bearer: test-api-key-123" (missing colon after Authorization)
    headers = {"Authorization Bearer": "test-api-key-123"}
    response = client_with_api_key.post("/", json={"text": "test"}, headers=headers)
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "not authorized"


def test_malformed_authorization_header_no_bearer(client_with_api_key):
    """Test Authorization header without Bearer prefix"""
    headers = {"Authorization": "test-api-key-123"}  # Missing "Bearer " prefix
    response = client_with_api_key.post("/", json={"text": "test"}, headers=headers)
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "not authorized"


def test_correct_authorization_header(client_with_api_key):
    """Test correct Authorization header format"""
    headers = {"Authorization": "Bearer test-api-key-123"}
    response = client_with_api_key.post("/", json={"text": "test"}, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)


def test_wrong_api_key(client_with_api_key):
    """Test wrong API key"""
    headers = {"Authorization": "Bearer wrong-api-key"}
    response = client_with_api_key.post("/", json={"text": "test"}, headers=headers)
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "not authorized"
