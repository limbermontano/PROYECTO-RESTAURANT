class restaurantSab:
    def __init__(self):
        self.codigo=[]
        self.nombre=[]
        self.precio=[]
        self.descripcionC=[]
        self.tipoC=[]
        self.descuento=[]
        self.habilitado=[]
        self.auto=0

    def pregunta(self):
        preg=input('DESEA VOLVER AL MENU PRINCIPAL:y/n \n')
        if  (preg=='y' or preg=='Y'):
            self.menuR()
        elif (preg=='n' or preg=='N'):
            self.salir()
        return '** POR FAVOR PRESIONE UNA OPCION **'

    def menuR(self):

        opcion="""
        ***** RESTAURANT EL BUEN SABOR *****
                ( MENU DEL SISTEMA )  
                     
        1.-REGISTRAR SERVICIO(COMIDAS)
        2.-MOSTRAR LISTADO DEL MENU
        3.-MOSTRAR LOS SERVICIOS DISPONIBLES DEL DIA
        4.-FILTRO DE SERVICIO POR PRODUCTO
        5.-MODIFICAR SERVICIOS REGISTRADOS
        6.-REGISTRO DE DESCUENTOS %
        7.-MODIFICAR PORCENTAJE
        8.-INABILITAR SERVICIO
        9.-HABILITAR SERVICIO
        10.-SALIR
        """
        print(opcion)
        print('***********************************************************************')
        seleccion=int(input('DIGITE UNA OPCION:\n'))
        if (seleccion== 1):
            print(self.resgPlat())
            print(self.menuR())
        elif (seleccion== 2):
            print(self.mostrarReg())
            print(self.pregunta())
        elif (seleccion== 3):
            print(self.mostrarReg())
            print(self.pregunta())
        elif (seleccion== 4):
            print(self.subopcionTip())
            print(self.pregunta())
        elif (seleccion== 5):
            print(self.modificarServ())
            print(self.pregunta())
        elif (seleccion== 6):
            print(self.registDes())
            print(self.pregunta())
        elif (seleccion== 7):
            print(self.modificarPorc())
            print(self.pregunta())
        elif (seleccion== 8):
            print(self.cambiarHabilitar())
            print(self.pregunta())
        elif (seleccion== 9):
            print(self.mostrarInab())
            print(self.habilitarServ())
            print(self.pregunta())
        elif (seleccion== 10):
            print(self.salir())

        else:
            print("** Digite una opción del Menú **")
            self.menuR()

    def activo(self):
        self.mostrarReg()
        codServ = int(input('INGRESE CODIGO DEL PLATO :\n '))
        posicion= self.codigo.index(codServ)
        return posicion
    def cambiarHabilitar(self):
        posicion=self.activo()
        return self.inabilitarServ(posicion)
    def inabilitarServ(self,posicion):
        self.habilitado[posicion]=0
        return ' EL PLATO {} SE INABILITADO CORRECTAMENTE'.format(self.nombre[posicion])
    def habilitarServ(self):
        codServ = int(input('INGRESE CODIGO :\n '))
        posicion = self.codigo.index(codServ)
        # return posicion
        # posicion=self.activo()
        self.habilitado[posicion] =1
        return ' EL PLATO {} SE HABILITO CORRECTAMENTE'.format(self.nombre[posicion])
    def modificarServ(self):

        posicion = self.buscarplato()
        dato = input("Desea modificar el nombre?: s/n \n")
        datoActual = self.nombre[posicion]
        nombre = self.confirmarEditarStr(dato, datoActual)
        dato = input("Desea modificar el precio?: s/n \n")
        datoActual = self.precio[posicion]
        precio = self.confirmarEditarInt(dato, datoActual)
        dato = input("Desea modificar la descripcion?: s/n \n")
        datoActual = self.descripcionC[posicion]
        descripcion = self.confirmarEditarStr(dato, datoActual)
        dato = input("Desea modificar el tipo de plato?: s/n \n")
        datoActual = self.tipoC[posicion]
        tipo = self.confirmarEditarStr(dato, datoActual)
        dato = input("Desea modificar el descuento?: s/n \n")
        datoActual = self.descuento[posicion]
        descuento = self.confirmarEditarInt(dato, datoActual)
        #preciofinal = self.descuentoPorcentaje(precio, descuento)
        self.guardarPlat(posicion, nombre, precio, descripcion, tipo, descuento)
        self.otros()
    def buscarplato(self):
        self.mostrarReg()
        print("-------------------------------")
        editar = int(input("Digite el codigo del plato a modificar: \n"))
        posicion = self.codigo.index(editar)
        self.descripcionMenu(posicion)
        return posicion
    def confirmarEditarStr(self,dato,datoActual):
        if(dato == 's' or dato == 'S'):
            nuevo = input("Ingrese el nuevo dato: \n")
            return nuevo
        elif(dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual
        else:
            print("** Seleccion erronea.!!! Regresando al menu modificar plato")
            self.menuR()
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
    def otros(self):
        otro = input("Desea modificar otro plato? s/n \n")
        if (otro == "s" or otro == "S"):
            self.modificarServ()
        if (otro == "n" or otro == "N"):
            return self.menuR()


# def codAutomatico(self):
#     if (self.auto < 100):
#         self.auto=self.auto +1
#         code='A0'+str(self.auto)
#         return code

    def subopcionTip(self):
        print('***** TIPO DE SERVICIO *****')
        opcion="""
        1.-DESAYUNO
        2.-ALMUERZO
        3.-CENA
        4.-POSTRE
        5.-VOLVER AL MENU
        """
        print(opcion)
        eleccion = int(input("DIGITE EL TIPO DE SERVICIO: \n"))
        if (eleccion ==1):
            self.descriProd('desayuno')
        elif (eleccion ==2):
            self.descriProd('almuerzo')
        elif (eleccion ==3):
            self.descriProd('cena')
        elif (eleccion ==4):
            self.descriProd('postre')
        elif (eleccion ==5):
            self.menuR()
    def resgPlat(self):
        codigo=int(input('Ingrese Codigo Por Favor: \n'))
        nombre=input('Ingrese plato del menu:\n')
        precio=int(input('Ingrese Precio:\n '))
        descripcionC=input('Ingrese Descripcion del plato a Servir:\n')
        tipoC=input('Ingrese Tipo de menu(desayuno, almuerzo, cena, postre:\n')
        descuento=int(input('Ingrese valor de descuento (%): \n'))
        #codigo=self.codAutomatico()
        print(self.guardarPlat(codigo,nombre.upper(),precio,descripcionC.upper(),tipoC.upper(),descuento))
        agregarmas=input('DESEA AGREGAR MAS TIPO DE PLATOS: y/n \n')
        if (agregarmas=='y' or agregarmas=='Y'):
            self.resgPlat()
        return'SE REGISTRO CORRECTAMENTE EL PLATO'
    def guardarPlat(self, cd,nb,pc,dp,tp,dt):
        self.codigo.append(cd)
        self.nombre.append(nb)
        self.precio.append(pc)
        self.descripcionC.append(dp)
        self.tipoC.append(tp)
        self.descuento.append(dt)
        self.habilitado.append(1)
        #print('EL PLATO {} SE REGISTRO CORRECTAMENTE').format(nombre)
        return"SE REGISTRO CON EXITO EL PLATO DE: {} **".format(nb)
    def mostrarReg(self):
        if (self.nombre):
            for i in range(len(self.nombre)):
                if (self.habilitado[i] == 1):
                    self.descripcionMenu(i)
                #return 'REGISTRO CARGADO CORRECTAMENTE'
        else:
            return 'ESTA VACIO EL REGISTRO'
    def descripcionMenu(self,hb):
       #if (self.habilitado[hb] ==1):
            print('**PLATO O MERIENDA  ***** {} *****'.format(self.nombre[hb]))
            print('CODIGO= {} '.format(self.codigo[hb]))
            print('PRECIO = {} Bs.'.format(self.precio[hb]))
            print('DESCRIPCION = ***{}***'.format(self.descripcionC[hb]))
            print('TIPO DE SERVICIO=** {} **'.format(self.tipoC[hb]))
            print('DESCUENTO = {} % '.format(self.descuento[hb]))
            print('ESTADO = {}'.format(self.habilitado[hb]))

            print('****************************************************')
    def modificarDes(self):

        self.mostrarReg()
        pocicion = int(input('INGRESE CODIGO :\n '))
        for i in range(len(self.nombre)):
             if (self.codigo[i] == pocicion):
                 poci = int(input('INGRESE MONTO  %:\n '))
                 self.descuento[i] = poci
                 self.descripcionMenu(i)
    def registDes(self):
        print("*******  REGISTRAR DESCUENTOS *******")
        self.modificarDes()
        return 'SE REGISTRO EL DESCUENTO  CORRECTAMENTE'
    def descriProd(self,sel):
       # self.subopcion()
        for i in range(len(self.nombre)):
            if (self.tipoC[i] ==sel.upper()):
                if (self.habilitado[i]==0):
                    pass
                else:
                    self.descripcionMenu(i)

        agregarmas = input('DESEA OTRO TIPO DE SERVICIO: y/n \n')
        if (agregarmas == 'y' or agregarmas == 'Y'):
            self.subopcionTip()
        else:
            self.menuR()

    def mostrarInab(self):
        print('*****PLATOS NO HABILITADOS******')
        if (self.nombre):
            for i in range(len(self.nombre)):
                if (self.habilitado[i] == 0):
                    self.descripcionMenu(i)
                    self.habilitado[i] = 1

                    return ' EL PLATO {} SE HABILITO CORRECTAMENTE'.format(self.nombre[i])
    def salir(self):
        return '*****GRACIAS POR UTILIZAR EL SISTEMA DEL RESTAURANT EL BUEN SABOR*****'
    def texto(self):
        print('ESTE SERVICIO ESTA EN OFERTA')
    def modificarPorc(self):
        print("*******  MODIFICAR PORCENTAJE *******")
        self.modificarDes()
        return 'PORCENTAJE MODIFICADO CORRECTAMENTE'

rest=restaurantSab()
rest.guardarPlat(1,'PICANTE',10,'PLATO PACEÑO PICANTE DE GALLINA CRIOLLA','ALMUERZO',0)
rest.guardarPlat(2,'KEPERI',15,'PLATO EXTRA','ALMUERZO',3)
rest.guardarPlat(3,'ENSALADA VITAMINADA',15,'DESAYUNO DE FRUTAS','DESAYUNO',0)
rest.guardarPlat(4,'JUGO DE FRUTILLA',18,'JUGO VITAMINADO','DESAYUNO',0)
rest.guardarPlat(5,'POLLO A LA BROASTER',25,'POLLO FRITO CON PAPAS','CENA',0)
rest.guardarPlat(6,'LOCRO',20,'LOCRO DE GALLINA CRIOLLA','CENA',0)
rest.guardarPlat(7,'FLAN',20,'FLAN CASERO','POSTRE',0)
rest.guardarPlat(8,'GELATINA',5,'GELATINA DE SABORES','POSTRE',0)
rest.menuR()






