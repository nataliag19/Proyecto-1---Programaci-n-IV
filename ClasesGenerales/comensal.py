class Comensal:
    
    _contador_comensal = 0

    MAPEO_SUBSIDIOS = {
        "alto": 0.5,
        "medio": 0.7, 
        "bajo": 0.9,  
        "ninguno": 1.0
    }

    def __init__(self, tipo_subsidio = "ninguno"):
        Comensal._contador_comensal += 1
        self.id_estudiante = Comensal._contador_comensal
        self.tipo_subsidio = tipo_subsidio

    def calcular_descuento(self, precio):
        multiplicador = self.MAPEO_SUBSIDIOS.get(self.tipo_subsidio, 1.0)
        return precio * multiplicador
