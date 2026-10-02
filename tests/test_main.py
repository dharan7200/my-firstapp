from app.main import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "python-demo-app"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "UP"


def test_ready():
    client = app.test_client()

    response = client.get("/ready")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "READY"


def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200
