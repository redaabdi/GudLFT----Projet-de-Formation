def test_unknown_email_does_not_crash(client):
    response = client.post('/showSummary', data={'email': 'inconnu@notexist.com'})

    assert response.status_code == 401
    assert b"Sorry, that email wasn't found." in response.data