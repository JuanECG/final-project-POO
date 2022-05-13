
import json


class Acta:

    def __init__(self,fecha,autor,nombre,tipo,director,jurado1,jurado2) -> None:
        self.fecha = fecha
        self.autor = autor
        self.nombre = nombre
        self.tipo = tipo
        self.director = director
        self.jurado1 = jurado1
        self.jurado2 = jurado2



    def __str__(self) -> str:
        return json.dump(self.__dict__)