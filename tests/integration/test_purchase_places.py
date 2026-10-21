from server import competitions, clubs
import html

def test_purchase_places_valid(client, clubs_for_test, competitions_for_test ): #happypath
    response = client.post('/purchasePlaces', data={"competition" : "Kyrox 2027", "club": "Fitnesspreneur", "places" : 3 })

    assert response.status_code == 200
    assert "Great-booking complete!" in html.unescape(response.data.decode())

def test_purchase_places_notenough_points(client, clubs_for_test, competitions_for_test): #sadpath
    response = client.post('/purchasePlaces', data={"competition" : "Kyrox 2027", "club": "Center Gym", "places" : 10 })

    assert response.status_code == 401
    assert "You don't have enough points !" in html.unescape(response.data.decode())

def test_purchase_places_old_competition(client, clubs_for_test, competitions_for_test):
    response = client.post('/purchasePlaces', data={"competition" : "PGW Bordeaux", "club": "Fitnesspreneur", "places" : 10 })

    assert response.status_code == 401
    assert "The competition ended !" in html.unescape(response.data.decode())