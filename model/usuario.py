
import json


class Usuario:
    next_id = 1

    def __init__(self, nombre, tipo="Estudiante") -> None:
        self.tipo = tipo
        self.nombre = nombre
        self._id = Usuario.next_id
        Usuario.next_id += 1

    def __str__(self) -> str:
        return json.dump(self.__dict__)
