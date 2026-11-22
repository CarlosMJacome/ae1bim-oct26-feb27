
from sqlalchemy import or_
from configuracion import obtener_sesion
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)


def consultar_or():
    sesion = obtener_sesion()

    try:
        print("\n=== CONSULTAS CON OR ===")

        # 1. Clinicas ubicadas en Quito o Machachi
        print("\n1. Clinicas ubicadas en Quito o Machachi:")
        clinicas = (
            sesion.query(Clinica)
            .filter(
                or_(
                    Clinica.direccion.contains("Quito"),
                    Clinica.direccion.contains("Machachi")
                )
            )
            .all()
        )

        for clinica in clinicas:
            print(f"{clinica.nombre} - {clinica.direccion}")

        # 2. Consultorios de cirugia o dermatologia
        print("\n2. Consultorios de cirugia o dermatologia:")
        consultorios = (
            sesion.query(Consultorio)
            .filter(
                or_(
                    Consultorio.especialidad == "Cirugia",
                    Consultorio.especialidad == "Dermatologia"
                )
            )
            .all()
        )

        for consultorio in consultorios:
            print(
                f"{consultorio.nombre} - "
                f"{consultorio.especialidad}"
            )

        # 3. Veterinarios llamados Carlos o Maria
        print("\n3. Veterinarios llamados Carlos o Maria:")
        veterinarios = (
            sesion.query(Veterinario)
            .filter(
                or_(
                    Veterinario.nombres == "Carlos",
                    Veterinario.nombres == "Maria"
                )
            )
            .all()
        )

        for veterinario in veterinarios:
            print(
                f"{veterinario.nombres} "
                f"{veterinario.apellidos}"
            )

        # 4. Historias clinicas con fractura o alergia
        print("\n4. Historias con diagnostico de fractura o alergia:")
        historias = (
            sesion.query(HistoriaClinica)
            .filter(
                or_(
                    HistoriaClinica.diagnostico.contains("Fractura"),
                    HistoriaClinica.diagnostico.contains("Alergia")
                )
            )
            .all()
        )

        for historia in historias:
            print(
                f"Mascota: {historia.nombre_mascota} "
                f"- Diagnostico: {historia.diagnostico}"
            )

    except Exception as error:
        print(f"Error al realizar consultas OR: {error}")

    finally:
        sesion.close()


if __name__ == "__main__":
    consultar_or()
