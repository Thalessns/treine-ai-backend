from sqlalchemy import (Column, String, Integer, ForeignKey)

from src.database.utils import Base


class CaloriasTable(Base):
    
    __tablename__ = "calorias"

    codigo = Column(String(length=255), primary_key=True)
    usuario = Column(String(length=255), ForeignKey("usuario.codigo"))
    carb_g = Column(Integer, nullable=False)
    prot_g = Column(Integer, nullable=False)
    gord_g = Column(Integer, nullable=False)
    total_kcal = Column(Integer, nullable=False)


calorias_table = CaloriasTable
