from server import error_purchase

clubs = [{
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points": "5"
    }, 
    {
        "name":"Summer Hit",
        "email":"john@summerhit.co",
        "points": "23"
    }
    ]

competition = {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }

def test_not_enough_points():
    assert error_purchase(clubs[0], competition, 10) == "You don't have enough points !"

def test_equal_points():
    assert error_purchase(clubs[0], competition, 5) == None

def test_more_points():
    assert error_purchase(clubs[0], competition, 3) == None

def test_less_12_places():
    assert error_purchase(clubs[1], competition, 11) == None

def test_equal_12_places():
    assert error_purchase(clubs[1], competition, 12) == None

def test_more_12_places():
    assert error_purchase(clubs[1], competition, 13) == "You can not book more than 12 places per competition !"

