from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from configuracion import cadena_base_datos

#Conexion a la base
engine = create_engine(cadena_base_datos)

#Clase base que heredan todas las tablas

Base = declarative_base()

#-------------CLASE 1

class Clinica(Base):
    __tablename__= 'clinicas'

    clinica_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(150), nullable=False)
    ciudad = Column(String(80), nullable=False)
    med_responsable = Column(String(100), nullable= False)


    #Relacion
    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return f"<Clinica(id={self.clinica_id}, nombre'{self.nombre}', ciudad'{self.ciudad}')>"

#-------------CLASE 2
class Consultorio(Base):
    __tablename__= 'consultorios'

    consultorio_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey('clinicas.clinica_id'), nullable=False)

    # Relaciones
    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return f"<Consultorio(id={self.consultorio_id}, nombre='{self.nombre}', especialidad='{self.especialidad}')>"


#-------------CLASE 3
class Veterinario(Base):
    __tablename__ = 'veterinarios'

    trabajador_id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    apellido = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    num_licencia = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey('consultorios.consultorio_id'), nullable=False)

    # Relaciones
    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return f"<Veterinario(id={self.trabajador_id}, nombre='{self.nombre} {self.apellido}')>"

    #-------------CLASE 4
class HistoriaClinica(Base):
    __tablename__ = 'historias_clinicas'

    historial_id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(200), nullable=False)
    nombre_mascota = Column(String(80), nullable=False)
    trabajador_id = Column(Integer, ForeignKey('veterinarios.trabajador_id'), nullable=False)

    # Relaciones
    veterinario = relationship("Veterinario", back_populates="historias")

    def __repr__(self):
        return f"<HistoriaClinica(id={self.historial_id}, mascota='{self.nombre_mascota}', fecha='{self.fecha}')>"


#Crea las tablas en veterinary.db 
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")





    #Por que el retun no hay self.diagnostico, tratamiento etc etc, porque no se esta llamando a la clase, sino que se esta creando un objeto de la clase, y el return es para mostrar la representacion del objeto, no para mostrar los atributos del objeto.