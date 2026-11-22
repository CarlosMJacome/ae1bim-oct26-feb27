
from configuracion import obtener_sesion
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)


def consultar_order_by():
    sesion = obtener_sesion()

    try:
        print("\n=== CONSULTAS CON ORDER_BY ===")

        # 1. Ordenar clinicas alfabeticamente
        print("\n1. Clinicas ordenadas por nombre:")
        clinicas = (
            sesion.query(Clinica)
            .order_by(Clinica.nombre.asc())
            .all()
        )

        for clinica in clinicas:
            print(f"{clinica.nombre} - {clinica.direccion}")

        # 2. Ordenar consultorios por especialidad
        print("\n2. Consultorios ordenados por especialidad:")
        consultorios = (
            sesion.query(Consultorio)
            .order_by(Consultorio.especialidad.asc())
            .all()
        )

        for consultorio in consultorios:
            print(
                f"{consultorio.nombre} - "
                f"Especialidad: {consultorio.especialidad}"
            )

        # 3. Ordenar veterinarios por apellido
        print("\n3. Veterinarios ordenados por apellido:")
        veterinarios = (
            sesion.query(Veterinario)
            .order_by(Veterinario.apellidos.asc())
            .all()
        )

        for veterinario in veterinarios:
            print(
                f"{veterinario.apellidos}, "
                f"{veterinario.nombres}"
            )

        # 4. Ordenar historias clinicas por fecha descendente
        print("\n4. Historias clinicas de mas reciente a antigua:")
        historias = (
            sesion.query(HistoriaClinica)
            .order_by(HistoriaClinica.fecha_atencion.desc())
            .all()
        )

        for historia in historias:
            print(
                f"{historia.fecha_atencion} - "
                f"{historia.nombre_mascota} - "
                f"{historia.diagnostico}"
            )

    except Exception as error:
        print(f"Error al ordenar registros: {error}")

    finally:
        sesion.close()


if __name__ == "__main__":
    consultar_order_by()
