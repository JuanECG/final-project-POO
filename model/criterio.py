import json


class Criterio:

    def __init__(self, id, descripcion,porcentaje,cal1,cal2,categoria)-> None:
        self.id = id
        self.descripcion = descripcion
        self.porcentaje = porcentaje
        self.calificacion1 = cal1
        self.calificacion2 = cal2
        self._categoria = categoria

    def __str__(self) -> str:
        return json.dump(self.__dict__)
