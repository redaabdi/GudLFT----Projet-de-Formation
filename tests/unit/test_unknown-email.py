import html

def test_unknown_email_does_not_crash(client):
    response = client.post('/showSummary', data={'email': 'inconnu@notexist.com'})

    assert response.status_code == 401
    assert "Sorry, that email wasn't found." in html.unescape(response.data.decode())

def test_empty_email_does_not_crash(client):
    response = client.post('/showSummary', data={'email': ''})
    
    assert response.status_code == 401
    assert "Please enter an email" in html.unescape(response.data.decode())