from server import competitions, clubs

def get_pair_club_have_less_points_than_competition() :
    club = min(clubs, key=lambda x: int(x["points"]))
    competition = max(competitions, key=lambda x: int(x["numberOfPlaces"]))
    return (club, competition)

competition = get_pair_club_have_less_points_than_competition()[1]
print(competition["name"])