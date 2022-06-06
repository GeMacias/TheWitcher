print("Bienvenido Al Almacen Don Julio")

total1=0
opcion1 =input("quiere llevar Agua: ")
if(opcion1== "si" or opcion1== "SI" or opcion1== "Si"):
    agua= int(input("cuanto agua desea: "))
    total1 = total1+ (600*agua)

total2=0
opcion2 =input("quiere llevar Azúcar: ")
if(opcion2== "si" or opcion2== "SI" or opcion2== "Si"):
    Azucar= int(input("cuanto azúcar desea: "))
    total2 = total2+ (1200*Azucar)

total3=0
opcion3 =input("quiere llevar Aceite: ")
if(opcion3== "si" or opcion3== "SI" or opcion3== "Si"):
    Aceite= int(input("cuanto Aceite desea: "))
    total3 = total3+ (1500*Aceite)

total4=0
opcion4 =input("quiere llevar Arroz: ")
if(opcion4== "si" or opcion4== "SI" or opcion4== "Si"):
    Arroz= int(input("cuanto Arroz desea: "))
    total4 = total4+ (1250*Arroz)

total5=0
opcion5 =input("quiere llevar Fideos: ")
if(opcion5== "si" or opcion5== "SI" or opcion5== "Si"):
    Fideos= int(input("cuanto Fideos desea: "))
    total5 = total5+ (790*Fideos)

total6=0
opcion6 =input("quiere llevar Bebida: ")
if(opcion6== "si" or opcion6== "SI" or opcion6== "Si"):
    Bebida= int(input("cuantas Bebidas desea: "))
    total6 = total6+ (1780*Bebida)

total7=0
opcion7 =input("quiere llevar Chocolate: ")
if(opcion7== "si" or opcion7== "SI" or opcion7== "Si"):
    Chocolate= int(input("cuanto Chocolate desea: "))
    total7 = total7+ (2500*Chocolate)

total8=0
opcion8 =input("quiere llevar Pan de Molde: ")
if(opcion8== "si" or opcion8== "SI" or opcion8== "Si"):
    Pan= int(input("cuanto Pan desea: "))
    total8 = total8+ (1340*Pan)

print("--------------------------------------------------------------")
total=total1+total2+total3+total4+total5+total6+total7+total8
print ("valor total",total)

cliente = input("Es Cliente Preferencial?: ")
if(cliente== "si" or cliente== "Si" or cliente== "Si"):
    print("Tiene un descuento del 25%")
    total = total*0.75
    print("El total con descuento es:",total)

efectivo=int(input("Ingrese el efectivo: "))
if efectivo>=total:
    total=efectivo-total
    print("su vuelto es:",total)
    print("Gracias por su compra")
if total>efectivo:
    print("Dinero Insuficiente, Gracias")
