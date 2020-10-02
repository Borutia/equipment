from sqlalchemy import Column, Integer, String, ForeignKey
from add_eqipment.database import Base


class Type_equipment(Base):
    __tablename__ = 'type_equipment'

    id = Column(Integer, primary_key=True)
    type_name = Column(String(200), nullable=False)
    mask_serial_number = Column(String(200), nullable=True)

    def __init__(self, type_name=None, mask_serial_number=None):
        self.type_name = type_name
        self.mask_serial_number = mask_serial_number


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    id_type_equipment = Column(Integer, ForeignKey('type_equipment.id'), nullable=False)
    serial_number = Column(String(200), unique=True, nullable=False)

    def __init__(self, id_type_equipment=None, serial_number=None):
        self.id_type_equipment = id_type_equipment
        self.serial_number = serial_number

