import uuid

class Ave:

    def __init__(self, nombre, raza, tamanio, precio, edad, color, tipoPlumas, *args, **kargs):
        self.nombre = nombre
        self.raza = raza
        self.tamanio = tamanio
        self.precio = precio
        self.edad = edad
        self.color = color
        self.tipoPlumas = tipoPlumas
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.tamanio}---{self.precio}---{self.edad}---" \
               f"{self.color}---{self.tipoPlumas}---{self.id}"
    
    def __repr__(self):
        return str(self.id)

    def cumpleAve(self, especificacion):
        dict_gato = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_gato or dict_gato[k] != especificacion.get_value(k):
                return False
        return True