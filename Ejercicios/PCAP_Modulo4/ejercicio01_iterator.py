class AlmacenMuebles:
    def __init__(self) -> None:
        self.stock = [('Cama',10),('Mesa',20),('Sillas',100),('Cabecero',0)]

    def __iter__(self):
        self.indice=-1
        return self
    
    def __next__(self):
        self.indice+=1
        if len(self.stock)==self.indice:
            raise StopIteration
        return self.stock[self.indice]

almacen = AlmacenMuebles()

for mueble in almacen:
    print(mueble)