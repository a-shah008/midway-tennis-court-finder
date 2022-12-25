from app import app, db
from app.models import TennisCourt

import random
import string

def create_random_string():
    uppercase_letters = []
    lowercase_letters = []
    numbers = []
    symbols = []

    for _ in range(2):
        uppercase_letters.append(random.choice(list(string.ascii_uppercase)))
        lowercase_letters.append(random.choice(list(string.ascii_lowercase)))
        numbers.append(random.choice([i for i in range(10)]))
        symbols.append(random.choice(list(string.punctuation)))

    create_string = uppercase_letters + lowercase_letters + numbers + symbols
    random.shuffle(create_string)
    final_string = ""

    for item in create_string:
        final_string += str(item)

    return final_string

def construct_courts():
    court_objs = []

    all_courts = TennisCourt.query.all()
    for existing_court in all_courts:
        db.session.delete(existing_court)
    db.session.commit()
    
    algonquin_middle_school_courts = TennisCourt(
        name="Algonquin Middle School", 
        address="599 Longwood Dr, Algonquin, IL, 60102",
        coordinates="42.15839818753812, -88.28275631552162",
        surface="Hard",
        num_of_courts=2,
        lighting=False,
        access="Public",
        other=None)
    gaslight_park_courts = TennisCourt(
        name="Gaslight Park",
        address="700 Terrace Dr, Algonquin, IL 60102",
        coordinates="42.1637507842632, -88.31262159013933",
        surface="Hard",
        num_of_courts=2,
        lighting=False,
        access="Public",
        other=None)
    crystal_lake_racket_club_courts = TennisCourt(
        name="Crystal Lake Racket Club",
        address="9101 S. Route 31, Algonquin, IL 60102",
        coordinates="42.19720642752417, -88.28949098399102",
        surface="Hard, Clay",
        num_of_courts=16,
        lighting=True,
        access="Public",
        other="Indoor Options, Pro Shop")
    harry_d_jacobs_high_school_courts = TennisCourt(
        name="Harry D. Jacobs High School",
        address="2601 Bunker Hill Dr, Algonquin, IL 60102",
        coordinates="42.16298242934268, -88.34347912473572",
        surface="Hard",
        num_of_courts=9,
        lighting=False,
        access="Public",
        other=None)
    grafelman_park_courts = TennisCourt(
        name="Grafelman Park",
        address="112 N 5th St, West Dundee, IL 60118",
        coordinates="42.09863472763808, -88.2829326311588",
        surface="Hard",
        num_of_courts=2,
        lighting=True,
        access="Public",
        other=None)
    centegra_health_bridge_courts = TennisCourt(
        name="Centegra Health Bridge Fitness Center",
        address="10450 Algonquin Rd, Huntley, IL 60142",
        coordinates="42.1762534637668, -88.40047647534253",
        surface="Hard",
        num_of_courts=4,
        lighting=True,
        access="Public",
        other="Indoor")

    db.session.add(algonquin_middle_school_courts)
    db.session.add(gaslight_park_courts)
    db.session.add(crystal_lake_racket_club_courts)
    db.session.add(harry_d_jacobs_high_school_courts)
    db.session.add(grafelman_park_courts)
    db.session.add(centegra_health_bridge_courts)
    db.session.commit()

    court_objs.append(algonquin_middle_school_courts)
    court_objs.append(gaslight_park_courts)
    court_objs.append(crystal_lake_racket_club_courts)
    court_objs.append(harry_d_jacobs_high_school_courts)
    court_objs.append(grafelman_park_courts)
    court_objs.append(centegra_health_bridge_courts)

    return court_objs
