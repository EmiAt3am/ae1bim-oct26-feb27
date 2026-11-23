from datetime import date
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Consultorio, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo 1: Consultorio que se llame -Consultorio 101- Y sea de -Medicina General-
consultorio_and = session.query(Consultorio).filter(
    and_(
        Consultorio.nombre == "Consultorio 101",
        Consultorio.especialidad == "Medicina General"
    )
).all()

print("- Consultorio 101 de Medicina General -")
for cons in consultorio_and:
    print(f"{cons.nombre} ({cons.especialidad}) - Clínica: {cons.clinica.nombre}")

# Ejemplo 2: Historias clinicas entre el 5 y el 12 de noviembre 2026
historias_rango = session.query(HistoriaClinica).filter(
    and_(
        HistoriaClinica.fecha >= date(2026, 11, 5),
        HistoriaClinica.fecha <= date(2026, 11, 12)
    )
).all()

print("\n -Historias Clínicas entre el 05/11/2026 y 12/11/2026- ")
for hist in historias_rango:
    print(f"{hist.fecha} | Mascota: {hist.nombre_mascota} | Diagnóstico: {hist.diagnostico}")

session.close()