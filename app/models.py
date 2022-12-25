from app import app, db

class TennisCourt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(500), unique=True)
    # Location - In terms of the coordinates of latitude and longitude:
    coordinates = db.Column(db.String(150), unique=True)
    # General Features and Other Ammenities
    surface = db.Column(db.String(150))
    num_of_courts = db.Column(db.Integer)
    lighting = db.Column(db.Boolean)
    access = db.Column(db.String(150))
    other = db.Column(db.String(150), default=None)

    def __repr__(self):
        return f"{self.name}"

