
import json


class Acta:
    next_id = 1

    def __init__(self) -> None:
        self._numero = Acta.next_id
        Acta.next_id += 1
        self.nombre = ""
        self.tipo = ""
        self.fecha = ""
        self.autor = ""
        self.director = ""
        self.jurado1 = ""
        self.jurado2 = ""



    def __str__(self) -> str:
        return json.dump(self.__dict__)