from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Veterinario, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

# Ordenar veterinarios de A a Z - apellido
veterinarios_ordenados = session.query(Veterinario).order_by(Veterinario.apellido).all()

print("Veterinarios ordenados por apellido (A - Z)")
for vet in veterinarios_ordenados:
    print(f"{vet.apellido}, {vet.nombre} - Consultorio: {vet.consultorio.nombre}")

# Ordenar historias por fecha, mas reciente a la antigua antigua
historias_recientes = session.query(HistoriaClinica).order_by(HistoriaClinica.fecha.desc()).all()

print("\n Historias Clinicas (mas recientes primero)")
for hist in historias_recientes:
    print(f"{hist.fecha} | Mascota: {hist.nombre_mascota} | Diagnóstico: {hist.diagnostico}")

session.close()