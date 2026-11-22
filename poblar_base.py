
from datetime import date
from sqlalchemy import select
from configuracion import obtener_sesion
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)


def poblar_base():
    sesion = obtener_sesion()

    try:
        # Evitar duplicar datos al ejecutar nuevamente
        if sesion.scalar(select(Clinica.id).limit(1)) is not None:
            print("La base de datos ya contiene clinicas.")
            return

        # Registrar clinicas
        clinicas = [
            Clinica(
                nombre="Veterinaria Patitas Felices",
                direccion="Quito, Av. Amazonas",
                veterinario_responsable="Carlos Ramirez"
            ),
            Clinica(
                nombre="Clinica AnimalCare",
                direccion="Machachi, Av. Amazonas",
                veterinario_responsable="Maria Lopez"
            ),
            Clinica(
                nombre="Centro Veterinario Huellitas",
                direccion="Ambato, Av. Cevallos",
                veterinario_responsable="Pedro Torres"
            )
        ]

        sesion.add_all(clinicas)
        sesion.flush()

        # Registrar consultorios
        consultorios = [
            Consultorio(nombre="Consultorio 1", especialidad="Medicina general", clinica_id=clinicas[0].id),
            Consultorio(nombre="Consultorio 2", especialidad="Cirugia", clinica_id=clinicas[0].id),
            Consultorio(nombre="Consultorio 3", especialidad="Dermatologia", clinica_id=clinicas[1].id),
            Consultorio(nombre="Consultorio 4", especialidad="Medicina general", clinica_id=clinicas[1].id),
            Consultorio(nombre="Consultorio 5", especialidad="Cirugia", clinica_id=clinicas[2].id),
            Consultorio(nombre="Consultorio 6", especialidad="Odontologia", clinica_id=clinicas[2].id)
        ]

        sesion.add_all(consultorios)
        sesion.flush()

        # Registrar veterinarios
        veterinarios = [
            Veterinario(nombres="Carlos", apellidos="Ramirez", correo="carlos@ejemplo.com", licencia_profesional="VET001", consultorio_id=consultorios[0].id),
            Veterinario(nombres="Ana", apellidos="Perez", correo="ana@ejemplo.com", licencia_profesional="VET002", consultorio_id=consultorios[1].id),
            Veterinario(nombres="Maria", apellidos="Lopez", correo="maria@ejemplo.com", licencia_profesional="VET003", consultorio_id=consultorios[2].id),
            Veterinario(nombres="Luis", apellidos="Gomez", correo="luis@ejemplo.com", licencia_profesional="VET004", consultorio_id=consultorios[3].id),
            Veterinario(nombres="Pedro", apellidos="Torres", correo="pedro@ejemplo.com", licencia_profesional="VET005", consultorio_id=consultorios[4].id),
            Veterinario(nombres="Sofia", apellidos="Mendoza", correo="sofia@ejemplo.com", licencia_profesional="VET006", consultorio_id=consultorios[5].id)
        ]

        sesion.add_all(veterinarios)
        sesion.flush()

        # Registrar historias clinicas
        datos_historias = [
            (date(2026, 11, 1), "Gripe canina", "Medicacion y reposo", "Max", 0),
            (date(2026, 11, 2), "Infeccion estomacal", "Dieta especial", "Luna", 0),
            (date(2026, 11, 3), "Fractura", "Cirugia y rehabilitacion", "Rocky", 1),
            (date(2026, 11, 4), "Herida superficial", "Limpieza y antibioticos", "Toby", 1),
            (date(2026, 11, 5), "Dermatitis", "Tratamiento topico", "Mia", 2),
            (date(2026, 11, 6), "Alergia", "Antihistaminicos", "Nala", 2),
            (date(2026, 11, 7), "Parasitos intestinales", "Desparasitacion", "Coco", 3),
            (date(2026, 11, 8), "Infeccion respiratoria", "Antibioticos", "Bobby", 3),
            (date(2026, 11, 9), "Lesion muscular", "Reposo y terapia", "Simba", 4),
            (date(2026, 11, 10), "Fractura de pata", "Cirugia", "Zeus", 4),
            (date(2026, 11, 11), "Gingivitis", "Limpieza dental", "Pelusa", 5),
            (date(2026, 11, 12), "Sarro dental", "Profilaxis dental", "Kira", 5)
        ]

        historias = [
            HistoriaClinica(
                fecha_atencion=fecha,
                diagnostico=diagnostico,
                tratamiento=tratamiento,
                nombre_mascota=mascota,
                veterinario_id=veterinarios[indice].id
            )
            for fecha, diagnostico, tratamiento, mascota, indice in datos_historias
        ]

        sesion.add_all(historias)
        sesion.commit()

        print("Datos ingresados correctamente.")
        print("3 clinicas registradas.")
        print("6 consultorios registrados.")
        print("6 veterinarios registrados.")
        print("12 historias clinicas registradas.")

    except Exception as error:
        sesion.rollback()
        print(f"Error al ingresar datos: {error}")

    finally:
        sesion.close()


if __name__ == "__main__":
    poblar_base()
