def Mezclador(string_a, string_b):
    s = a[0:2] + b[-2:]
    print(s)
    return s

a = "pelo"
b = "loro"
Mezclador(a,b)

a="votar"
b= a.replace("v","n")
print(b)

a = "oso pardo"
b = a.strip("o")
print(b)

def intercalar(string_a, string_b):
    i = 0
    cadena = ""
    while (i < len(a)):

        cadena = cadena + a[i] + b


        i = i + 1
    return cadena


a = "familia"
b = "so"
print(intercalar(a, b))

def ocurrencias(string):
  r = string.count("1") - string.count("0")
  return r
string = "11000110101"
print(ocurrencias(string))



def reemplazar_mayusculas(cadena):
    i = 0
    while i<len(cadena):
        if cadena[i].isupper():
            cadena = cadena.replace(cadena[i], '$')
        i+=1
    return cadena

cadena= "Hola Mundo"
print (reemplazar_mayusculas(cadena))

