from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica, Consultorio

Session = sessionmaker(bind=engine)
session = Session()


clinicas_quito = session.query(Clinica).filter(Clinica.ciudad == "Quito").all()

print("=== Clínicas en Quito ===")
for clinica in clinicas_quito:
    print(f"Clínica: {clinica.nombre} - Dirección: {clinica.direccion} ({clinica.ciudad})")

# filtrar consultorios y navegar objeto clinica
consultorios_gen = session.query(Consultorio).filter(Consultorio.especialidad == "Medicina General").all()

print("\n=== Consultorios de Medicina General ===")
for cons in consultorios_gen:
    print(f"{cons.nombre} ({cons.especialidad}) - Clínica: {cons.clinica.nombre}")

session.close()