## EL SOULS DEFINITIVO

Nombre:str= "Teloki-totodo"
Vitalidad:int= 100
if Vitalidad <1:
    Vitalidad= 1
elif Vitalidad >100:
    Vitalidad= 100 

Stamina:int= 100
if Stamina <0:
    Stamina= 0
elif Stamina >100:
    Stamina= 100

Nivel:int= 1
if Nivel <1:
    Nivel= 1

Almas:int= 1000
if Almas <0:
    Almas= 0

Estus:int= 3
if Almas <0:
    Almas= 0

Arma:str= "Colmillo de Sabueso"

print(Nombre)
print("Tienes",Vitalidad,"puntos de Vitalidad y",Stamina,
      "puntos de Stamina")

print(Nombre,"ejecuta tremendo ataque en salto" \
" con tremenda robada de pájaro aérea y resulta herido al caer perdiendo " \
"Vitalidad y Stamina....")

Daño_caida:int=15
Vitalidad= Vitalidad-Daño_caida
Stamina:int= Stamina-Daño_caida
print(Vitalidad)
print(Stamina)





