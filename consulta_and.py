
from sqlalchemy import and_
from configuracion import obtener_sesion
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)


def consultar_and():
    sesion = obtener_sesion()

    try:
        print("\n=== CONSULTAS CON AND ===")

        # 1. Clinicas ubicadas en Quito y con responsable Carlos Ramirez
        print("\n1. Clinicas de Quito con responsable Carlos Ramirez:")
        clinicas = (
            sesion.query(Clinica)
            .filter(
                and_(
                    Clinica.direccion.contains("Quito"),
                    Clinica.veterinario_responsable == "Carlos Ramirez"
                )
            )
            .all()
        )

        for clinica in clinicas:
            print(
                f"{clinica.nombre} - "
                f"Responsable: {clinica.veterinario_responsable}"
            )

        # 2. Consultorios de medicina general de la clinica 2
        print("\n2. Consultorios de medicina general de la clinica 2:")
        consultorios = (
            sesion.query(Consultorio)
            .filter(
                and_(
                    Consultorio.especialidad == "Medicina general",
                    Consultorio.clinica_id == 2
                )
            )
            .all()
        )

        for consultorio in consultorios:
            print(
                f"{consultorio.nombre} - "
                f"Especialidad: {consultorio.especialidad}"
            )

        # 3. Veterinarios llamados Maria con licencia VET003
        print("\n3. Veterinarios llamados Maria con licencia VET003:")
        veterinarios = (
            sesion.query(Veterinario)
            .filter(
                and_(
                    Veterinario.nombres == "Maria",
                    Veterinario.licencia_profesional == "VET003"
                )
            )
            .all()
        )

        for veterinario in veterinarios:
            print(
                f"{veterinario.nombres} {veterinario.apellidos} "
                f"- Licencia: {veterinario.licencia_profesional}"
            )

        # 4. Historias clinicas de fractura elaboradas por veterinario 2
        print("\n4. Historias de fractura del veterinario 2:")
        historias = (
            sesion.query(HistoriaClinica)
            .filter(
                and_(
                    HistoriaClinica.diagnostico.contains("Fractura"),
                    HistoriaClinica.veterinario_id == 2
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
        print(f"Error al realizar consultas AND: {error}")

    finally:
        sesion.close()


if __name__ == "__main__":
    consultar_and()
