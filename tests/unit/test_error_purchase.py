from server import error_purchase

club = {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    }

competition = {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }

def test_not_enough_points():
    assert error_purchase(club, competition, 15) == "You don't have enough points !"

def test_enough_points():
    assert error_purchase(club, competition, 10) == None