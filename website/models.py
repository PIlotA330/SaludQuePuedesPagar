from website import db

class PDM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    facility_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    services = db.Column(db.String(120), nullable=False)
    facility_type = db.Column(db.String(120), nullable=False)
    dental = db.Column(db.String(2), nullable=False)
    mental = db.Column(db.String(2), nullable=False)
    primary = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f"PDM('{self.city}', '{self.address}', '{self.zip}', '{self.facility_name}', '{self.phone}', '{self.services}', '{self.facility_type}', '{self.dental}', '{self.mental}', '{self.primary}')"