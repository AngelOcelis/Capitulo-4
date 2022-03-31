asistentes = 0
men = 0
women = 0
edadmen = 0
edadwomen = 0
repetir = 's'
edad = 0
edadmin = 0

while repetir=='s' or repetir=='S':
    genero = 0
    edad = int (input ('Ingresa Porfavor Su Edad: '))
    if edad<18:
        print ('No se permiten menores de edad a la fiesta.')    
    else:
        edadmin = min(edadmin,edad)
        asistentes+=1
        print ('Selecciona El Genero.')
        print (' 1.- Mujer')
        print(' 2.- Hombre')
        while genero != 1 and genero != 2:
            genero = int (input (' : '))
            if genero != 1 and genero != 2:
                print('Valor Incorrecto. Intente Nuevamente.')
        if genero==1 and edad>=18:
            women+=1
            edadwomen += edad
        if genero==2 and edad>=18:
            men+=1
            edadmen += edad
    if edad != 0:
        repetir = str(input('Deseas repetir el proceso? (S/N):'))
    else:
        break
print('Asistentes A La Fiesta:',men+women)
print('Número De Hombres:', men)
print('Número de Mujeres', women)
if men > 0:
    print(f'Edad Promedio Hombres,{edadmen/men: 2f}' )
if women > 0:
    print(f'Edad Promedio Mujeres,{edadwomen/women: 2f}')
    print('Persona Más Joven',edadmin)
