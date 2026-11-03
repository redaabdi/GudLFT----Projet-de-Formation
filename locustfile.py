from locust import HttpUser, task, between, events

# Nombre d'achats d'1 place pendant un test.
# Doit rester <= 12 (limite par club et par compétition) et <= points du club
# et <= places de la compétition.
NB_ACHATS = 10


@events.test_start.add_listener
def remise_a_zero(environment, **kwargs):
    ClubUser.achats = 0

class ClubUser(HttpUser):
    wait_time = between(1, 3)
    achats = 0

    @task
    def chargement_accueil(self):
        self.client.get("/")

    @task
    def chargement_connexion(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def mise_a_jour(self):
        if ClubUser.achats < NB_ACHATS:
            ClubUser.achats += 1
            self.client.post("/purchasePlaces", data={"club": "Simply Lift", "competition": "Fally", "places": 1})