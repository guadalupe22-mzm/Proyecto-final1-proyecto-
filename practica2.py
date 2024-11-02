print ("Verificacion de promedios")

cantidad = int(input("Digite la cantidad de examenes:"))
if cantidad>3:
    print("No puedes agregar mas de tres examenes")
    
else: 
    notas1 = int(input("Digite la primera nota: "))
    notas2 = int(input("Digite la segunda nota: "))
    if cantidad == 3:
        notas3 = int(input("Digite la tercera nota: "))
    else:
        notas3 = 0
        
    promedio = (notas1 + notas2 + notas3)/ cantidad 
    print("Su promedio es de : ", promedio)
    if promedio >= 70:
        print ("APROBASTE") 
        
    if promedio < 70  and promedio >=60:
        print ("TIENES QUE HACER AMPLIACION") 
                
    if promedio <60:
        print ("REPROBASTE ") 
        

    