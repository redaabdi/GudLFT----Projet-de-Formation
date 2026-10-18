from server import get_club_by_email, clubs

#sadpath
def test_get_club_by_email_unknown():
    assert get_club_by_email("inconnu@notexist.com", clubs) == None

def test_get_club_by_email_empty():
    assert get_club_by_email("", clubs) == None
    assert get_club_by_email(None, clubs) == None

#happypath
def test_get_club_by_email_valid():
    assert get_club_by_email(clubs[0]['email'], clubs) == clubs[0]
