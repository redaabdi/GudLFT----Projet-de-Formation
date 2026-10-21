from server import get_club_by_email

#sadpath
def test_get_club_by_email_unknown(clubs_for_test):
    assert get_club_by_email("inconnu@notexist.com", clubs_for_test) == None

def test_get_club_by_email_empty(clubs_for_test):
    assert get_club_by_email("", clubs_for_test) == None
    assert get_club_by_email(None, clubs_for_test) == None

#happypath
def test_get_club_by_email_valid(clubs_for_test):
    assert get_club_by_email(clubs_for_test[0]['email'], clubs_for_test) == clubs_for_test[0]
