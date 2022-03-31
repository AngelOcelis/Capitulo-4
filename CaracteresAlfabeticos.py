alfabeto=('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
texto=input("Digite Una Palabra:  ")
contar=0

for i in texto:
    if i in alfabeto:
        contar+=1
    else:
        print("La Palabra No Tiene Caracteres Alfabeticos")
        break
if contar==len(texto):
        print("La Palabra Tiene Caracteres Alfabeticos")     