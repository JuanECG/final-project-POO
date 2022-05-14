import json
from model.criterio import Criterio


class Evaluacion:

    def __init__(self) -> None:
        super().__init__()
        self.criterios = []       
        self.observaciones = ""
        self.nota = 0.0

        # Datos de toda evaluacion
        self.fecha_evaluacion = ""
        self.nombre_estudiante = ""
        self.id_estudiante = ""
        self.tema_proyecto = ""
        self.version_doc = " "  # Identifica la version en la que va la evaluación

        # Llamado al método que inicializa la información precargada
        self._inicializar_criterios()

    def _inicializar_criterios(self):

        # Abrir datos JSON
        f = open('../data/criterios.json')

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
