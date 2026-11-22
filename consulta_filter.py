
from configuracion import obtener_sesion
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)


def consultar_filter():
    sesion = obtener_sesion()

    try:
        print("\n=== CONSULTAS CON FILTER ===")

        # 1. Buscar clinicas ubicadas en Quito
        print("\n1. Clinicas ubicadas en Quito:")
        clinicas = (
            sesion.query(Clinica)
            .filter(Clinica.direccion.contains("Quito"))
            .all()
        )

        for clinica in clinicas:
            print(f"{clinica.nombre} - {clinica.direccion}")

        # 2. Buscar consultorios de medicina general
        print("\n2. Consultorios de medicina general:")
        consultorios = (
            sesion.query(Consultorio)
            .filter(Consultorio.especialidad == "Medicina general")
            .all()
        )

        for consultorio in consultorios:
            print(
                f"{consultorio.nombre} - "
                f"Clinica: {consultorio.clinica.nombre}"
            )

        # 3. Buscar veterinario por licencia profesional
        print("\n3. Veterinario con licencia VET003:")
        veterinarios = (
            sesion.query(Veterinario)
            .filter(Veterinario.licencia_profesional == "VET003")
            .all()
        )

        for veterinario in veterinarios:
            print(
                f"{veterinario.nombres} {veterinario.apellidos} "
                f"- {veterinario.correo}"
            )

        # 4. Buscar historias clinicas con diagnostico de fractura
        print("\n4. Historias clinicas relacionadas con fracturas:")
        historias = (
            sesion.query(HistoriaClinica)
            .filter(HistoriaClinica.diagnostico.contains("Fractura"))
            .all()
        )

        for historia in historias:
            print(
                f"Mascota: {historia.nombre_mascota} "
                f"- Diagnostico: {historia.diagnostico}"
            )

    except Exception as error:
        print(f"Error al realizar consultas: {error}")

    finally:
        sesion.close()


if __name__ == "__main__":
    consultar_filter()
