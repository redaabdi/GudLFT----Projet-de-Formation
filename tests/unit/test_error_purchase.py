from server import error_purchase

clubs = [{
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points": "5"
    }, 
    {
        "name":"Summer Hit",
        "email":"john@summerhit.co",
        "points": "30"
    }
    ]

competitions = [{
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {
            "name": "Festival of joy",
            "date": "2020-03-28 10:00:00",
            "numberOfPlaces": "10",
        }
        ]

def test_not_enough_points():
    assert error_purchase(clubs[0], competitions[0], 10) == "You don't have enough points !"

def test_equal_points():
    assert error_purchase(clubs[0], competitions[0], 5) == None

def test_more_points():
    assert error_purchase(clubs[0], competitions[0], 3) == None

def test_less_12_places():
    assert error_purchase(clubs[1], competitions[0], 11) == None

def test_equal_12_places():
    assert error_purchase(clubs[1], competitions[0], 12) == None

def test_more_12_places():
    assert error_purchase(clubs[1], competitions[0], 13) == "You can not book more than 12 places per competition !"

def test_less_places_than_competition():
    assert error_purchase(clubs[1], competitions[1], 9) == None

def test_equal_places_than_competition():
    assert error_purchase(clubs[1], competitions[1], 10) == None

def test_more_places_than_competition():
    assert error_purchase(clubs[1], competitions[1], 11) == "You can not book more than the max of the competition !"