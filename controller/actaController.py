class ActaController:
    def __init__(self) -> None:
        super().__init__()
        # FIXME convertirlo en diccionario cuya llave sea el id del estudiante y el valor una lista de las evaluaciones que se han hecho para el mismo estudiante
        self.actas = []

    def agregar_acta(self, acta):        
        self.actas.append(acta)
    
    def getActaNombre(self,nombre):
        for acta in self.actas:
            if acta.nombre == nombre:
                return acta
        return ""
