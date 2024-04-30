import random
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, link, producto, cantidad):
      
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "codigo": producto.descripcion,
                "acumulado": cantidad *producto.precio,
                "cantidad": cantidad,
                "link": link,
                "imagen": str(producto.imagen),
                "precio": producto.precio,
                "precioanterior": int(producto.precio *1.25),
            }
       
        else:
           
            id = str(int(id)+random.randint(1,100000))
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": cantidad *producto.precio,
                "codigo": producto.descripcion,
                "cantidad": cantidad,
                "link": link,
                "imagen": str(producto.imagen),
                "precio": producto.precio,
                "precioanterior": int(producto.precio *1.25),
            }
        
        print(link)
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
    def limpiaritem(self, producto):
        self.eliminar(str(producto))
        self.session.modified = True