import json


class Criterio:
    next_id = 1

    def __int__(self, descripcion, categoria)-> None:
        self._descripcion = descripcion
        self._categoria = categoria
        self._id = Criterio.next_id
        Criterio.next_id += 1

    def __str__(self) -> str:
        return json.dump(self.__dict__)
