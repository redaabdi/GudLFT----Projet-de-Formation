import pytest
import server
from server import app

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def clubs_for_test(monkeypatch):
    data = [
        {"name": "Fitnesspreneur", "email": "fitnesspreneur@test.com", "points": "13"},
        {"name": "Center Gym", "email": "centergym@test.com", "points": "4"},
        {"name": "Essential Flow", "email": "essentialflow@test.com", "points": "24"}
    ]
    monkeypatch.setattr(server, "clubs", data)
    return data


@pytest.fixture
def competitions_for_test(monkeypatch):
    data = [
        {"name": "Kyrox 2027", "date": "2027-03-27 10:00:00", "numberOfPlaces": "25", "soldHistory" : []},
        {"name": "ZONE LIFT 2027", "date": "2027-03-27 10:00:00", "numberOfPlaces": "5", "soldHistory" : []},
        {"name": "PGW Bordeaux", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25", "soldHistory" : []}
    ]
    monkeypatch.setattr(server, "competitions", data)
    return data