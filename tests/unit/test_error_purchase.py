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
    },
    {
        "name":"Perform sleep repeat",
        "email":"ronaldinho@perform.co",
        "points": "20"
    }
    ]

competitions = [{
            "name": "Spring Festival",
            "date": "2027-03-27 10:00:00",
            "numberOfPlaces": "25",
            "soldHistory" : [["Summer Hit", 7],[ "Simply Lift", 3], ["Summer Hit", 3]]
        },
        {
            "name": "Kyrox",
            "date": "2027-03-28 10:00:00",
            "numberOfPlaces": "10",
            "soldHistory" : []
        },
        {
            "name": "Kyrox 2024",
            "date": "2024-03-28 10:00:00",
            "numberOfPlaces": "10",
            "soldHistory" : []
                }
        ]

def test_not_enough_points():
    assert error_purchase(clubs[0], competitions[0], 10) == "You don't have enough points !"

def test_equal_points():
    assert error_purchase(clubs[0], competitions[0], 5) == None

def test_more_points():
    assert error_purchase(clubs[0], competitions[0], 3) == None

def test_less_12_places_once():
    assert error_purchase(clubs[2], competitions[0], 11) == None

def test_equal_12_places_once():
    assert error_purchase(clubs[2], competitions[0], 12) == None

def test_more_12_places_once():
    assert error_purchase(clubs[2], competitions[0], 13) == "You can not book more than 12 places per competition !"

def test_equal_12_places_total():
    assert error_purchase(clubs[1], competitions[0], 2) == None

def test_more_12_places_total():
    assert error_purchase(clubs[1], competitions[0], 3) != None

def test_less_places_than_competition():
    assert error_purchase(clubs[1], competitions[1], 9) == None

def test_equal_places_than_competition():
    assert error_purchase(clubs[1], competitions[1], 10) == None

def test_more_places_than_competition():
    assert error_purchase(clubs[1], competitions[1], 11) == "You can not book more than the max of the competition !"

def test_old_competition() :
    assert error_purchase(clubs[1], competitions[2], 3) == "The competition ended !"

def test_not_old_competition() :
    assert error_purchase(clubs[1], competitions[1], 3) == None

def test_book_negative_places():
    assert error_purchase(clubs[0], competitions[0], -3) == "Please enter a positive number"

def test_book_string_place():
    assert error_purchase(clubs[0], competitions[0], "str") == "Please enter an integer number"

def test_book_decimal_number_string_place():
    assert error_purchase(clubs[0], competitions[0], "2.3") == "Please enter an integer number"

def test_book_integer_string_place():
    assert error_purchase(clubs[0], competitions[0], "2") == None