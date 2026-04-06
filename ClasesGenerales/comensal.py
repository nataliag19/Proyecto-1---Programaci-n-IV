class Comensal:
    
    _contador_comensal = 0

    def __init__(self, tipo_subsidio):
        Comensal._contador_comensal += 1
        self.id_estudiante = Comensal._contador_comensal
        self.tipo_subsidio = tipo_subsidio or ""

    def calcular_descuento(self, precio):
        if self.tipo_subsidio == "alto":
            return precio * 0.5
        elif self.tipo_subsidio == "medio":
            return precio * 0.7
        elif self.tipo_subsidio == "bajo":
            return precio * 0.9
        return precio
