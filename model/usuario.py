
import json


class Usuario:

    def __init__(self,nombre,tipo="Estudiante") -> None:        
        self.tipo = tipo
        self.nombre = nombre

        
    def __str__(self) -> str:
        return json.dump(self.__dict__)