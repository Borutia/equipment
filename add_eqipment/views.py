from flask import Blueprint, request, jsonify
from add_eqipment.add_equipment import get_all_type_equipment, add_equipment_textarea

add_equipment = Blueprint('add_equipment', __name__)


@add_equipment.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = get_all_type_equipment()
        return jsonify(data)
    if request.method == 'POST':
        data = request.get_json()
        type_equipment = int(data['type_equipment'])
        textarea = data['textarea'].split('\n')
        check_add = add_equipment_textarea(type_equipment, textarea)
        log = ''
        for _ in check_add:
            log += _
        data = {'error': log}
        return jsonify(data)
