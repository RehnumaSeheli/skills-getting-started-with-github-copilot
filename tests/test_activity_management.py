from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activities["Chess Club"]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in activities["Chess Club"]["participants"]


def test_unregister_participant_raises_404_for_missing_student():
    activities["Chess Club"]["participants"] = ["daniel@mergington.edu"]

    response = client.delete("/activities/Chess Club/participants/missing@mergington.edu")

    assert response.status_code == 404
