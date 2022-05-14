import json
from model.criterio import Criterio

class Acta:
    next_id = 1

    def __init__(self) -> None:        
        self._numero = Acta.next_id
        Acta.next_id += 1
        self.id_estudiante = ""
        self.nombre = ""
        self.tipo = ""
        self.fecha = ""
        self.autor = ""
        self.director = ""
        self.version_doc = ""
        self.nota = 0.0
        self.jurado1 = ""
        self.jurado2 = ""
        self.criterios=[]
        self.observaciones = []

        # Llamado al método que inicializa la información precargada
        self._inicializar_criterios()

    def _inicializar_criterios(self):

        # Abrir datos JSON
        f = open('./data/criterios.json')

        # Retorna objeto JSON como diccionario
        data = json.load(f)

        for item in data["criterios"]:
            criterio = Criterio(
                item["id"],
                item["descripcion"],
                item["porcentaje"],
                item["calificacion1"],
                item["calificacion2"],
                item["categoria"]
            )
            self.criterios.append(criterio)
            
    def __str__(self) -> str:
        return json.dumps(self.__dict__)

        # TODO completar con el resto de criterios
