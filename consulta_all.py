from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica 

Session = sessionmaker(bind=engine)
session = Session()

# all trae todos los objs de clinica

clinicas = session.query(Clinica).all()

print('Clinicas y numero de historias asociadas:')
for clinica in clinicas:
    total_historias = 0

    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias)

    print(f"Clínica: {clinica.nombre} ({clinica.ciudad}) -> Historias Clínicas: {total_historias}")

session.close()

