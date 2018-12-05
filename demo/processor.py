from datetime import datetime

from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


import helpers as h
import persistence

db = persistence.db
bp = Blueprint('processor', __name__)


@bp.route('/charge', methods=('POST',))
def create_charge():
    """Returns POST Data."""
    extracted = h.get_dict(
        'url', 'args', 'form', 'data', 'origin', 'headers', 'files', 'json')
    charge_entry = Charge.from_dict(extracted['json'])
    db.session.add(charge_entry)
    db.session.commit()
    return h.jsonify(extracted)


class Charge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    card_number = db.Column(db.String(100))
    card_expiration = db.Column(db.String(100))
    card_security_code = db.Column(db.String(100))
    amount = db.Column(db.Integer)

    @classmethod
    def from_dict(cls, entry):
        charge_obj = cls()
        charge_obj.card_number = entry['card']
        charge_obj.card_expiration = entry['card_expiration']
        charge_obj.card_security_code = entry['card_security_code']
        charge_obj.amount = entry['amount']
        return charge_obj


class ChargeView(ModelView):
    pass


def init_app(app):
    app.register_blueprint(bp)
    app.json_encoder = h.JSONEncoder

    processor_admin = Admin(app,
                            url='/processor_admin',
                            endpoint='/processor_admin',
                            name='Processor Portal',
                            base_template='processor/admin/base.html',
                            template_mode='bootstrap3')
    processor_admin.add_view(ChargeView(
        Charge, db.session, endpoint='charges'))
    return app
