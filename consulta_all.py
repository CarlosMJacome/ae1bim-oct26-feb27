
from sqlalchemy import func
from configuracion import obtener_sesion
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)


def consultar_clinicas():
    sesion = obtener_sesion()

    try:
        # Obtener todas las clinicas usando all()
        clinicas = sesion.query(Clinica).all()

        print("\n=== LISTADO DE CLINICAS ===")

        for clinica in clinicas:
            # Contar las historias clinicas asociadas
            total_historias = (
                sesion.query(func.count(HistoriaClinica.id))
                .join(Veterinario)
                .join(Consultorio)
                .filter(Consultorio.clinica_id == clinica.id)
                .scalar()
            )

            print(f"\nClinica: {clinica.nombre}")
            print(f"Direccion: {clinica.direccion}")
            print(f"Veterinario responsable: {clinica.veterinario_responsable}")
            print(f"Total de historias clinicas: {total_historias}")

        # Mostrar tambien los registros de las otras entidades
        print("\n=== CONSULTORIOS ===")
        for consultorio in sesion.query(Consultorio).all():
            print(
                f"{consultorio.nombre} - {consultorio.especialidad} "
                f"- Clinica: {consultorio.clinica.nombre}"
            )

        print("\n=== VETERINARIOS ===")
        for veterinario in sesion.query(Veterinario).all():
            print(
                f"{veterinario.nombres} {veterinario.apellidos} "
                f"- Licencia: {veterinario.licencia_profesional}"
            )

        print("\n=== HISTORIAS CLINICAS ===")
        for historia in sesion.query(HistoriaClinica).all():
            print(
                f"Mascota: {historia.nombre_mascota} "
                f"- Diagnostico: {historia.diagnostico}"
            )

    except Exception as error:
        print(f"Error al consultar: {error}")

    finally:
        sesion.close()


if __name__ == "__main__":
    consultar_clinicas()
