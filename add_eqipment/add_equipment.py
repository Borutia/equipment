from add_eqipment.database import db_session
from add_eqipment.models import Equipment, Type_equipment
import re


def get_all_type_equipment():
    query_all = db_session.query(Type_equipment.type_name).all()
    data = {}
    for counter, element in enumerate(query_all):
        data[counter + 1] = element[0]
    return data


def create_mask_regex(type_equipment):
    mask_param = {
        'N': '\d',
        'A': '[A-Z]',
        'a': '[a-z]',
        'X': '([A-Z]|\d)',
        'Z': '(\-|\_|\@)'
    }
    mask_regex = ''
    exist_mask = db_session.query(Type_equipment).filter_by(id=type_equipment).first()
    for _ in exist_mask.mask_serial_number:
        mask_regex += mask_param[_]
    mask_regex += '$'
    return mask_regex


def add_equipment_textarea(type_equipment, textarea):
    mask_regex = create_mask_regex(type_equipment)
    log = []
    for text in textarea:
        if re.match(mask_regex, text) is not None:
            exist_serial_number = db_session.query(Equipment).filter_by(serial_number=text).first()
            if not exist_serial_number:
                create_equipment = Equipment(id_type_equipment=type_equipment, serial_number=text)
                db_session.add(create_equipment)
                db_session.commit()
            else:
                log.append(text + ' уже существует. ')
        else:
            log.append(text + ' нет соответсвия с маской. ')
    return log

