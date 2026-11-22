
from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuracion de la base de datos SQLite
DATABASE_URL = "sqlite:///veterinaria.db"

# Crear el motor de conexion
engine = create_engine(DATABASE_URL, echo=False)

# Habilitar las claves foraneas en SQLite
@event.listens_for(engine, "connect")
def activar_claves_foraneas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Clase base para definir las entidades
Base = declarative_base()

# Configurar las sesiones de la base de datos
Session = sessionmaker(bind=engine)

# Funcion para obtener una sesion
def obtener_sesion():
    return Session()
