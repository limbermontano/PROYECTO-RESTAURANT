
class restaurante:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.precio = []
        self.precioFinal = []
        self.descripcion = []
        self.tipo = []
        self.descuento = []
        self.habilitado = []
        self.estado = []
        self.cod = 0

    def menu(self):
        opciones= """
     *** 🐚 Restaurante El Crustáceo Crujiente 🐚 ***

              1.- Registrar Plato
              2.- Deshabilitar plato 
              3-. Listado de platos
              4.- Modificar Plato
              5.- Modificar Descuento
              6.- Mostrar tipo de platos
              7.- Mostrar menú del dia
              8.- Habilitar platos inactivos
              9.- Salir
        """
        print(opciones)
        eleccion = input("Elija una opción del menú: \n")
        if self.numero(eleccion):
            elegir = int(eleccion)
        else:
            print("** Digite solo números **")
            self.menu()
        self.opcion(elegir)

    def numero(self, eleccion):
        if eleccion.isdigit():
            return True
        else:
            return False

    def opcion(self ,elegir):
        if (elegir == 1):
            print(self.registrarPlato())
            print(self.menu())
        elif (elegir == 2):
            print(self.habilitados())
            print(self.volverAlMenu())
        elif (elegir == 3):
            print(self.mostrar())
            print(self.volverAlMenu())
        elif (elegir == 4):
            print(self.editar())
            print(self.volverAlMenu())
        elif (elegir == 5):
            print(self.modificarDesc())
            print(self.volverAlMenu())
        elif (elegir == 6):
            print(self.buscar())
            print(self.volverAlMenu())
        elif (elegir == 7):
            print(self.mostrarMenuDia())
            print(self.volverAlMenu())
        elif (elegir == 8):
            print(self.habilitarInactivos())
            print(self.volverAlMenu())
        elif (elegir == 9):
            print(self.salir())
        elif (elegir == 9):
            print(self.salir())
        else:
            print("** Digite una opción del Menú **")
            self.menu()
        pass

    def volverAlMenu(self):
        elegir = input("¿Desea volver al menú? s/n: \n")
        if (elegir == "s" or elegir == "S"):
            return self.menu()
        else:
            return "** Gracias por utilizar el sistema v1.0.1 **"

    def guardar(self, codigo, nombre, precio, descripcion, tipo, descuento, preciofinal):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.precio.append(precio)
        self.descripcion.append(descripcion)
        self.tipo.append(tipo)
        self.descuento.append(descuento)
        self.precioFinal.append(preciofinal)
        self.habilitado.append(1)
        self.estado.append(1)
        return "** {} fue registrado correctamente **".format(nombre)

    def descuentoPorcentaje(self,precio,descuento):
        porciento = (precio * descuento) / 100
        preciofinal = precio - porciento
        return preciofinal

    def validarInt(self,dato):
        if(dato.isdigit()):
            dato = int(dato)
            return dato
        else:
            print("** Digite solo numeros **")
            return self.menu()

    def registrarPlato(self):
        nombre = input("Nombre del plato: \n")
        precio = input("Precio del plato: \n")
        precio = self.validarInt(precio)
        descripcion = input("Descripción del plato: \n")
        tipo = input("Tipo de plato: desayuno/almuerzo/cena/postre \n")
        descuento = input("Descuento: \n")
        descuento = self.validarInt(descuento)
        codigo = self.code()
        preciofinal = self.descuentoPorcentaje(precio,descuento)
        print(self.guardar(codigo, nombre, precio, descripcion, tipo, descuento,preciofinal))
        otro = input("¿Desea registrar otro plato? s/n \n")
        if (otro == "s" or otro == "S"):
            self.registrarPlato()
        return "*** Plato registrado correctamente! ***"

    def habilitados(self):
        if self.nombre:
            self.mostrar()
            print("-------------------------------")
            pregunta = input("¿Qué plato desea deshabilitar? \n")
            posicion = self.nombre.index(pregunta)
            print(self.cambioHabilitado(posicion))
            otro = input("Desea deshabilitar otro plato? s/n \n")
            if (otro == "s" or otro == "S"):
                self.habilitados()
            elif (otro == "n" or otro == "N"):
                self.menu()
        else:
            return "**** La lista del menú se encuentra vacia *** "

    def cambioHabilitado(self, posicion):
        self.habilitado[posicion] = 0
        return "Deshabilitado exitosamente"

    def detallePlatos(self, posicion):
        if (self.estado[posicion] == 1):
            print("-------------------------------")
            print("     **** {} ****".format(self.nombre[posicion]))
            print("Código: {}".format(self.codigo[posicion]))
            print("Precio: {} Bs.".format(self.precio[posicion]))
            print("Descuento: {}% ".format(self.descuento[posicion]))
            if (int(self.descuento[posicion]) > 0):
                print("***** OFERTA *****")
            else:
                print("** NO TIENE OFERTA **")
            print("Precio con descuento: {} Bs.".format(self.precioFinal[posicion]))
            print("Descripción: {}".format(self.descripcion[posicion]))
            print("Tipo: {}".format(self.tipo[posicion]))
            if (self.habilitado[posicion] == 1):
                print("habilitado: si")
            elif (self.habilitado[posicion] == 0):
                print("habilitado: No")
            pass

    def mostrar(self):
        if (self.nombre):
            for i in range(len(self.nombre)):
                self.detallePlatos(i)
            return "-------------------------------"
        else:
            return "**** La lista de los menus se encuentra vacia *** "
        pass

    def buscarplato(self):
        self.mostrar()
        print("-------------------------------")
        editar = input("Digite el codigo del plato a modificar: \n")
        posicion = self.codigo.index(editar)
        self.detallePlatos(posicion)
        return posicion

    def editar(self):
        posicion = self.buscarplato()
        dato = input("Desea modificar el nombre?: s/n \n")
        datoActual = self.nombre[posicion]
        nombre = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el precio?: s/n \n")
        datoActual = self.precio[posicion]
        precio = self.confirmarEditarInt(dato,datoActual)
        dato = input("Desea modificar la descripcion?: s/n \n")
        datoActual = self.descripcion[posicion]
        descripcion = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el tipo de plato?: s/n \n")
        datoActual = self.tipo[posicion]
        tipo = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el descuento?: s/n \n")
        datoActual = self.descuento[posicion]
        descuento = self.confirmarEditarInt(dato,datoActual)
        preciofinal = self.descuentoPorcentaje(precio,descuento)
        self.guardarModificacion(posicion,nombre,precio,descripcion,tipo,descuento,preciofinal)
        self.otros()

    def confirmarEditarStr(self,dato,datoActual):
        if(dato == 's' or dato == 'S'):
            nuevo = input("Ingrese el nuevo dato: \n")
            return nuevo
        elif(dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual
        else:
            print("** Seleccion erronea.!!! Regresando al menu modificar plato")
            self.menu()

    def confirmarEditarInt(self,dato,datoActual):
        if(dato == 's' or dato == 'S'):
            nuevo = int(input("Ingrese el nuevo dato: \n"))
            return nuevo
        elif(dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual
        else:
            print("** Seleccion erronea.!!! Regresando al menu modificar plato")
            self.menu()

    def guardarModificacion(self,posicion,nombre,precio,descripcion,tipo,descuento,preciofinal):
        self.nombre[posicion] = nombre
        self.precio[posicion] = precio
        self.descripcion[posicion] = descripcion
        self.tipo[posicion] = tipo
        self.descuento[posicion] = descuento
        self.precioFinal[posicion] = preciofinal
        return "** Actualizado correctamente.!!! **"


    def otros(self):
        otro = input("Desea modificar otro plato? s/n \n")
        if (otro == "s" or otro == "S"):
            self.editar()
        if (otro == "n" or otro == "N"):
            return self.menu()

    def otrosDesc(self):
        otro = input("Desea modificar otro plato? s/n \n")
        if (otro == "s" or otro == "S"):
            self.modificarDesc()
        if (otro == "n" or otro == "N"):
            return self.menu()

    def buscar(self):
        buscar1 = False
        buscar = input("¿Qué menú desea ver? desayuno/almuerzo/cena/postre \n")
        for i in range(len(self.nombre)):
            if (self.tipo[i] == buscar):
                if(self.habilitado[i] == 1):
                    self.detallePlatos(i)
                    buscar1 = True
        if(buscar1 == False):
            print("** Aún no hay platos de ese tipo en el menú **")
        print("-------------------------------")
        buscar2 = input("¿Desea ver otro menú? s/n \n")
        if (buscar2 == "s" or buscar2 == "S"):
            self.buscar()
        elif (buscar2 == "n" or buscar2 == "N"):
            self.menu()
        return "  *********************** "

    def mostrarMenuDia(self):
        mostrar = False
        for i in range(len(self.nombre)):
            if (self.habilitado[i] == 1):
                self.detallePlatos(i)
                mostrar = True
        if (mostrar == False):
            return "** no hay ningún plato disponible **"
        else:
            return "-------------------------------"

    def code(self):
        if (self.cod >= 10):
            self.cod = self.cod + 1
            codigo = "0" + str(self.cod)
            return codigo
        elif (self.cod < 10):
            self.cod = self.cod + 1
            codigo = "00" + str(self.cod)
            return codigo

    def modificarDesc(self):
        posicion = self.buscarplato()
        confirmar = input("** Esta seguro que desea modificar el descuento actual?: s/n \n")
        if(confirmar == 's' or confirmar == 'S'):
            descuento = int(input("Ingrese el nuevo descuento: \n"))
            return self.confirmarDesc(descuento,posicion)
        else:
            print("** Sin cambios realizados **")
            return self.menu()

    def confirmarDesc(self,descuento,posicion):
        self.descuento[posicion] = descuento
        precio = self.precio[posicion]
        preciofinal = self.descuentoPorcentaje(precio,descuento)
        self.precioFinal[posicion] = preciofinal
        print("** Descuento modificado exitosamente **")
        return self.otrosDesc()

    def habilitarInactivos(self):
        confirmar = input("Desea habilitar los platos inactivos?: s/n \n")
        if(confirmar == 's' or confirmar == 'S'):
            return self.buscarInabilitados()
        else:
            return "** No existen platos inabilitados **"

    def buscarInabilitados(self):
        for posicion in range(len(self.nombre)):
            if (self.habilitado[posicion] == 0):
                self.habilitar(posicion)
        return "** Platos habilitados exitosamente"

    def habilitar(self,posicion):
        self.habilitado[posicion] = 1
    def salir(self):
        return '*****"** Gracias por utilizar el sistema v1.0.1 **"*****'

restaurante = restaurante()
restaurante.menu()





