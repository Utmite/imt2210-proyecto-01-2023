from copy import deepcopy, copy

class Vec:
    def __init__(self, dominio: list, coordenadas: dict) -> None:
        self.D = dominio

        if any(key not in self.D for key in coordenadas.keys()):
            raise ValueError("Hay ejes en cords que no estan en el domineo")

        self.f = coordenadas
    
    def __borrar_ceros(self):
        for k, v in deepcopy(self.f).items():
            if v == 0:
                del self.f[k]

    def getitem(self, k):
        if k not in self.D:
            raise ValueError(f"El eje {k} no existe en el domineo: {self.D}")
        return self.f.get(k, 0)
    
    def setitem(self, k, v):
        if k not in self.D:
            raise ValueError(f"El eje {k} no existe en el domineo: {self.D}")

        self.__borrar_ceros()

        self.f[k] = v

    def equal(self, u):
        return self.D == u.D and self.f == u.f
    
    def add(self, u):
        if self.D != u.D:
            raise ValueError("No tienen el mismo domineo")
        salida = Vec(deepcopy(self.D), deepcopy(self.f)) 

        for i in self.D:
            salida.setitem(i, self.getitem(i) + u.getitem(i))

        salida.__borrar_ceros()

        return salida
    
    def dot(self, u):
        if self.D != u.D:
            raise ValueError("No tienen el mismo domineo")
        r = 0
        for i in self.D:
            r += self.getitem(i) * u.getitem(i)
        return r
    
    def scalar_mul(self, alpha):
        salida = Vec(deepcopy(self.D), deepcopy(self.f)) 
        for i in self.D:
            salida.setitem(i, salida.getitem(i) * alpha)

        salida.__borrar_ceros()

        return salida
    
    def neg(self):
        salida = Vec(deepcopy(self.D), deepcopy(self.f)) 
        for i in self.D:
            salida.setitem(i,  salida.getitem(i) * -1)
        return salida

    def __str__(self) -> str:
        self.__borrar_ceros()
        return f"Vec({self.D},{self.f})"


def main():
    v = Vec(["x", "y", "z"], {"x":1, "y": 3})
    u = Vec(["x", "y", "z"], {"y":2, "z":3})
    z = Vec(["x", "y", "z"], {"x":1, "y": 5, "z": 3})
    w = Vec(["w", "u"], {"w":10, "u": 5})


    assert v.equal(u) == False

    assert v.getitem("z") == 0
    assert v.getitem("x") == 1

    v.setitem("x", 99)
    assert v.getitem("x") == 99
    v.setitem("x", 0)
    assert v.getitem("x") == 0
    v.setitem("x", 0)
    v.setitem("x", 1)
    assert v.getitem("x") == 1

    assert v.add(u).equal(z) == True

    assert v.add(u).add(z.neg()).equal(Vec(dominio=["x", "y", "z"], coordenadas={}))
    assert v.dot(z) == 16
    assert v.dot(z.neg()) == -16
    assert z.neg().scalar_mul(-1).equal(z)
    assert w.scalar_mul(12).equal(Vec(["w", "u"], {"w":120, "u": 60}))
    print("Paso todos los test")
if __name__ == "__main__":
    main()


#
# 1 * 0 + 3 * 2 + 
#
#






