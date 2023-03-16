from datetime import datetime
from malcheck_dash.config import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(16))
    emp_id = db.Column(db.String(16), index=True)
    name = db.Column(db.String(64), index=True)
    platform_os = db.Column(db.String(16))
    status = db.Column(db.String(16))
    signature = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_dict(self):
        return {
            'address': self.address,
            'emp_id': self.emp_id,
            'name': self.name,
            'platform_os': self.platform_os,
            'status': self.status,
            'signature': self.signature,
            'timestamp': self.timestamp
        }
