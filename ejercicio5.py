#Somos los dueños de un videoclub (sí, en pleno siglo XXI) y queremos
# representar los valores que caracterizan a una película dentro de nuestro
# videoclub. Para ello necesitamos los siguientes datos:
# Título de la película.------
# Año de estreno.
# Duración en minutos.
# País de estreno.
# Nombre y apellidos de director/a.
# Género (Por ejemplo: “Acción”).
# Puntuación en IMDB (puede contener números con decimales).


Tit_Pel:str= "Guardianes de la Galaxia Volumen 1"
Año_ES:int= 2014
Dura:int= 140
País_ES:str= "Estados Unidos"
Nombre_completo_Dir:str= "James Gunn"
Género:str="Acción/Ciencia Ficción"
Puntos_IMDB:float= 8


print("!!!!Bienvenido al videoclub sirena!!!!")
print("----LA PELICULA DE LA SEMANA ES:----")
print(Tit_Pel)
print("Duración",Dura,"minutos")
print("Se estrenó en",País_ES)
print("Pertence al director",Nombre_completo_Dir)
print("Género: ",Género)
print("Puntuación IMDB:",Puntos_IMDB,"estrellas")


