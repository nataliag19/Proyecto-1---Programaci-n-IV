class Plato:
    def __init__(self, nombre = "Plato Default", precio = 1000, veg = False, cantidad = 1):
        self.nombre = nombre
        self._precio_base = precio
        self.es_vegetariano = veg
        self.cantidad = cantidad

    def precio(self):
        return self._precio_base

    def esta_disponible(self):
        return self.cantidad > 0

    def reducir_stock(self):
        if self.cantidad > 0:
            self.cantidad -= 1

    def descripcion_detallada(self):
        tipo = "Vegetariano" if self.es_vegetariano else "Normal"
        estado = "Disponible" if self.esta_disponible() else "Agotado"
        return f"{self.nombre} | {tipo} | ${self._precio_base} | {estado} | Stock: {self.cantidad}"
