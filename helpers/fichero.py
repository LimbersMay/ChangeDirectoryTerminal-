# Clase que se encarga de leer el fichero de configuración del Json y extraerá los datos
import json
from io import open


class Fichero:
    def __init__(self, ruta):
        self.ruta = ruta
        self.cargar = None

    def guardar_valor(self, clave, valor):
        # Abrimos el fichero y cargamos la información en formato json
        with open(self.ruta, "r") as fichero:
            self.cargar = json.loads(fichero.read())

        # Modificamos la información del Json
        self.cargar[clave] = valor

        # Guardamos la información nuevamente en el fichero Json
        with open(self.ruta, "w") as fichero:
            fichero.write(json.dumps(self.cargar, indent=4))

    def obtener_valor(self, clave):
        # Abrimos el fichero y cargamos la información en formato json
        with open(self.ruta, "r") as fichero:
            self.cargar = json.loads(fichero.read())

        # Devolvemos la información solicitada
        return self.cargar[clave]

    def listar_valores(self):
        # Abrimos el fichero y cargamos la información en formato json
        with open(self.ruta, "r") as fichero:
            self.cargar = json.loads(fichero.read())

        return self.cargar

    def eliminar_valor(self, clave):
        # Cargamos el fichero
        with open(self.ruta, "r") as fichero:
            self.cargar = json.loads(fichero.read())

        del self.cargar[clave]

        # Guardamos nuevamente el fichero
        with open(self.ruta, "w") as fichero:
            fichero.write(json.dumps(self.cargar, indent=4))