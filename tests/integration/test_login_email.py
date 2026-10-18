import html
from server import clubs

def test_login_fail(client):
    response = client.post('/showSummary', data={'email': 'inconnu@notexist.com'})

    assert response.status_code == 401
    assert "Sorry, that email wasn't found." in html.unescape(response.data.decode())

def test_login_valid(client):
    response = client.post('/showSummary', data={'email': clubs[0]['email']})
    
    assert response.status_code == 200