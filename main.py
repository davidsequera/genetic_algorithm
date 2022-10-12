import random 

def foo(x,y,z):
    return 2*x**2 +y**2 + 5*z - 25 # Se quiere encontrar las variables que satisface la ecuación

def fitness(x,y,z) : #Determina que tan optima es la solución
    respuesta = foo(x,y,z)

    if respuesta == 0: #Si la solución es 0, es una solución optima
        return 99999
    else: 
        return abs(1/respuesta) #Define que tan cercana la respuesta llega a 0

#Se genera las soluciones aleatoriamente

soluciones = []
for s in range(1000):
    soluciones.append((random.uniform(0,10000),random.uniform(0,10000),random.uniform(0,10000))) 
    #x,y,z

#Genetic algorithm
#Generar una generación 

for i in range (10000): # numero de generaciones

    clsoluciones = []
    for s in soluciones: #se recorre la lista de solucionnes
        clsoluciones.append((fitness(s[0],s[1],s[2]),s)) #contiene las soluciones que se obtenieron de la función fitness + la tupla de los parametros
    clsoluciones.sort()
    clsoluciones.reverse()

    print(f"Generacion : {i} , mejores soluciones: " )
    print( clsoluciones[0])

    if clsoluciones[0][0] > 999: #si las soluciones son lo suficientemente buenas se detiene el ciclo
        break

    mejoresoluciones = clsoluciones[:100] #se toman únicamente las mejores 100 parametros para la solucion

    elementos = []

    for s in mejoresoluciones: 
        elementos.append( s[1][0]  ) #se extraen todos los parametros que se usaron para la función
        elementos.append( s[1][1]  )
        elementos.append( s[1][2]  )

    #se combinan las nuevas soluciones
    ngeneracion = []
    for i in range(1000):
        e1 = random.choice(elementos) * random.uniform(0.99,1.01)# Se mutan las soluciones 
        e2 = random.choice(elementos) * random.uniform(0.99,1.01)
        e3 = random.choice(elementos) * random.uniform(0.99,1.01)

        ngeneracion.append( (e1,e2,e3)) #se crea una nueva tupla co tods los elementos

    soluciones = ngeneracion    
#for s in soluciones: #se recorre la lista de solucoines
 #      print(s)

