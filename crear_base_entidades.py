from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from configuracion import cadena_base_datos

#Conexion a la base
engine = create_engine(cadena_base_datos)

#Clase base que heredan todas las tablas

class Clinica(Base):
    __tablename__= 'clinicas'

    clinica_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(150), nullable=False)
    ciudad = Column(String(80), nullable=False)
    med_responsable = Column(String(100), nullable= False)