from random import randint
numeros=[]

contador=0
 #Creacion de lista con 100 numeros #1
for i in range(100):
    numeros.append(randint(0,10)) # llenando la lista
    print(numeros)

# Mostrar por pantalla sólo los valores que se encuentren en los índices pares
for i in range(len(numeros)):                          #2
    if i %2==0:#Solo se muestren indices pares
        print(f"posicion {i}   {numeros[i]}")

# Mostrar numero mayor
mayor=max(numeros)
print(f"el numero mayor es {mayor}")

#Mostrar el índice (posición) del elemento mayor
print("indices o coordenadas donde se encuentra el numero mayor")
for i in range (len(numeros)):
    if numeros[i]==max(numeros):
        print(i, end= " ⭐ ")
print(" ")

#Mostrar el índice (posición) del elemento menor
print("indices o coordenadas donde se encuentra el numero mayor")
for i in range (len(numeros)):
    if numeros[i]==min(numeros):
        print(i, end= " ❤️❤️  ")
print(" ")


# Mostrar numero menor
menor=min(numeros)
print(f"el numero menor es {menor}")








