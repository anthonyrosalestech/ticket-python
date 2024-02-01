from flask import Blueprint, jsonify
from models.TicketModel import TicketModel

main = Blueprint('aspazul_blueprint', __name__)


@main.route('/aspazul')
def get_data():
    try:
        tickets = TicketModel.get_tickets()
        return jsonify(tickets), 200
    except Exception as ex:
        return jsonify({'msg': str(ex)}), 500
