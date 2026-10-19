from server import competitions, clubs
import html

def get_pair_club_have_less_points_than_competition() :
    club = min(clubs, key=lambda x: int(x["points"]))
    competition = max(competitions, key=lambda x: int(x["numberOfPlaces"]))
    return (club, competition)

def test_purchase_places_enough_points(client): #happypath
    club = get_pair_club_have_less_points_than_competition()[0]
    competition = get_pair_club_have_less_points_than_competition()[1]
    response = client.post('/purchasePlaces', data={"competition" : competition["name"], "club": club["name"], "places" : 1 })

    assert response.status_code == 200
    assert "Great-booking complete!" in html.unescape(response.data.decode())

def test_purchase_places_above_points(client): #sadpaths
    club = get_pair_club_have_less_points_than_competition()[0]
    competition = get_pair_club_have_less_points_than_competition()[1]
    response = client.post('/purchasePlaces', data={"competition" : competition["name"], "club": club["name"], "places" : int(club["points"])+1 })

    assert response.status_code == 401
    assert "Error : You don't have enough points !" in html.unescape(response.data.decode())
