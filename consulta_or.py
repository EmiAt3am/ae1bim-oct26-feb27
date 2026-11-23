from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

# Traer clinicas en Quito o en Cuenca
clinicas_or = session.query(Clinica).filter(
    or_(
        Clinica.ciudad == "Quito",
        Clinica.ciudad == "Cuenca"
    )
).all()

print("-Clinicas en Quito o Cuenca-")
for clinica in clinicas_or:
    print(f"{clinica.nombre} - Ciudad: {clinica.ciudad}")

# Ejemplo: historias clinicas de la mascota = Luna O Mau Lou
historias_or = session.query(HistoriaClinica).filter(
    or_(
        HistoriaClinica.nombre_mascota == "Luna",
        HistoriaClinica.nombre_mascota == "Mau Lou"
    )
).all()

print("\n Historias Clínicas de Luna o Mau Lou ")
for hist in historias_or:
    print(f"{hist.fecha} | Mascota: {hist.nombre_mascota} | Veterinario: {hist.veterinario.nombre} {hist.veterinario.apellido}")

session.close()


