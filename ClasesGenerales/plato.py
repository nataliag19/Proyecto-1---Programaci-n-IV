class Plato:
    def __init__(self, args_plato):
        self.nombre = args_plato.get('nombre', 'Plato Default')
        self._precio_base = args_plato.get('precio', 1000)
        self.es_vegetariano = args_plato.get('plato_veg', False)
        self.cantidad = args_plato.get('cantidad', 1)

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
