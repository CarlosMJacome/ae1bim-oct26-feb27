
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from configuracion import Base, engine


# Entidad Clinica
class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return f"Clinica(id={self.id}, nombre='{self.nombre}')"


# Entidad Consultorio
class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)

    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return f"Consultorio(id={self.id}, nombre='{self.nombre}')"


# Entidad Veterinario
class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    licencia_profesional = Column(String(50), nullable=False, unique=True)

    consultorio_id = Column(
        Integer, ForeignKey("consultorios.id"), nullable=False
    )

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica", back_populates="veterinario"
    )

    def __repr__(self):
        return f"Veterinario(id={self.id}, nombres='{self.nombres}')"


# Entidad Historia Clinica
class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(250), nullable=False)
    tratamiento = Column(String(250), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)

    veterinario_id = Column(
        Integer, ForeignKey("veterinarios.id"), nullable=False
    )

    veterinario = relationship(
        "Veterinario", back_populates="historias_clinicas"
    )

    def __repr__(self):
        return (
            f"HistoriaClinica(id={self.id}, "
            f"mascota='{self.nombre_mascota}')"
        )


# Crear las tablas en la base de datos
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tablas creadas correctamente en veterinaria.db")
