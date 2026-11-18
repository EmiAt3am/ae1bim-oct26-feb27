from datetime import date
from sqlalchemy import sessionmaker

from crear_base_entidades import engine, Clinica, Consultorio, Veterinario, HistoriaClinica

#crear comunicacion con la base
Session = sessionmaker(bind=engine)
session = Session()

#clinicas para varias ciudades
clinica1 = Clinica(
    nombre='Clinica Veterinaria Con Patitas',
    direccion='Av. Amazonas N24-120',
    ciudad='Quito',
    med_responsable='Dr. Carlos Mendoza'
)
clinica2 = Clinica(
    nombre='Clinica Veterinaria Patitas Felices',
    direccion='Av. 9 de Octubre 450',
    ciudad='Guayaquil',
    med_responsable='Dra. Valeria Torres'
)
clinica3 = Clinica(
    nombre='Clinica Veterinaria Peluditos',
    direccion='Calle Larga 8-30',
    ciudad='Cuenca',
    med_responsable='Dr. Andrés Paredes'
)

#Consultorios 
cons1 = Consultorio(
    nombre='Consultorio 101',
    especialidad='Medicina General',
    clinica=clinica1
)
cons2 = Consultorio(
    nombre='Consultorio 102',
    especialidad='Cirugia',
    clinica=clinica1
)
cons3 = Consultorio(
    nombre='Consultorio A',
    especialidad='Dermatologia',
    clinica=clinica2
)
cons4 = Consultorio(
    nombre='Consultorio 103',
    especialidad='Medicina General',
    clinica=clinica3
)

#Veterinarios
vet1 = Veterinario(
    nombre='Lucia',
    apellido='Pérez',
    email='lucia.gomez@patitas.ec',
    num_licencia='VET-1001',
    consultorio=cons1
)
vet2 = Veterinario(
    nombre="Mateo", 
    apellido="Ríos",
    email="mateo.rios@patitas.ec", 
    num_licencia="VET-1002",
    consultorio=cons2
)
vet3 = Veterinario(
    nombre="Sofía", 
    apellido="Vega",
    email="sofia.vega@animalsur.ec", 
    num_licencia="VET-2001",
    consultorio=cons3
)
vet4 = Veterinario(
    nombre="Diego", 
    apellido="Castro",
    email="diego.castro@losandes.ec", 
    num_licencia="VET-3001",
    consultorio=cons4
)

#Historias Clinicas 
hist1 = HistoriaClinica(
    fecha=date(2026,11, 2),
    diagnostico='Gastroenteritis leve',
    tratamiento='Dieta blanda e hidratación por 3 días',
    nombre_mascota='Mau Lou',
)
hist2 = HistoriaClinica(
    fecha=date(2026, 11, 5),
    diagnostico="Control de vacunas",
    tratamiento="Refuerzo vacuna séxtuple",
    nombre_mascota="Luna",
    veterinario=vet1
)
hist3 = HistoriaClinica(
    fecha=date(2026, 11, 8),
    diagnostico="Fractura en pata delantera",
    tratamiento="Inmovilización quirúrgica y analgésicos",
    nombre_mascota="Max",
    veterinario=vet2
)
hist4 = HistoriaClinica(
    fecha=date(2026, 11, 10),
    diagnostico="Dermatitis alérgica",
    tratamiento="Shampoo medicado y antihistamínico",
    nombre_mascota="Michi",
    veterinario=vet3
)
hist5 = HistoriaClinica(
    fecha=date(2026, 11, 12),
    diagnostico="Otitis externa",
    tratamiento="Gotas óticas antibióticas por 7 días",
    nombre_mascota="Toby",
    veterinario=vet3
)
hist6 = HistoriaClinica(
    fecha=date(2026, 11, 14),
    diagnostico="Chequeo preventivo",
    tratamiento="Desparasitación interna",
    nombre_mascota="Lula",
    veterinario=vet4
)

#Agregar los objetos a la sesión
session.add_all([clinica1, clinica2, clinica3, 
                 cons1, cons2, cons3, cons4, 
                 vet1, vet2, vet3, vet4, 
                 hist1, hist2, hist3, hist4, hist5, hist6])
session.commit()
session.close()

print("Los datos fueron ingresados correctamente en la base de datos.")
