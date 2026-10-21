import html

def test_login_fail(client, clubs_for_test, competitions_for_test):
    response = client.post('/showSummary', data={'email': 'inconnu@notexist.com'})

    assert response.status_code == 401
    assert "Sorry, that email wasn't found." in html.unescape(response.data.decode())

def test_login_valid(client, clubs_for_test, competitions_for_test):
    response = client.post('/showSummary', data={'email': clubs_for_test[0]['email']})
    
    assert response.status_code == 200