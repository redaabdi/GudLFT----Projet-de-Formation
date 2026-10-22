import html

def test_full_journey(client, clubs_for_test, competitions_for_test):
    club = clubs_for_test[0]
    competition = competitions_for_test[0]
    points_before = int(club["points"])
    places_before = int(competition["numberOfPlaces"])

    response = client.post("/showSummary", data={"email": club["email"]})
    assert response.status_code == 200
    assert competition["name"] in response.data.decode()

    response = client.get(f"/book/{competition['name']}/{club['name']}")
    assert response.status_code == 200

    response = client.post("/purchasePlaces", data={"competition": competition["name"], "club": club["name"], "places": 3})
    assert "Great-booking complete!" in html.unescape(response.data.decode())

    # Effets visibles
    assert int(club["points"]) == points_before - 3
    assert int(competition["numberOfPlaces"]) == places_before - 3

    assert client.get("/logout").status_code == 302