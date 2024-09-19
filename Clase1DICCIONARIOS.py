# 1 Crear un dicccionario que contenga nombre, edad y carrera de un alumno y mostrar el diccionario completo.

Alumno1={"Nombre":"Julian","Edad":"23","Carrera":"Prof. de Educacion Fisica"}

print(Alumno1)
# 2 utilizar el metodo get para mostrar el valor de la calve nombre 

Alumno1={"Nombre":"Julian","Edad":"23","Carrera":"Prof. de Educacion Fisica"}

print("El nombre del alumno es",Alumno1.get("Nombre"))

# 3 cambiar la edad del alumno y mostrar el diccionario completo

Alumno1["Edad"] = "35"
print(Alumno1)

# 4 agregar un par clave valor que contenga el sexo alumno, mostrar el diccionario completo.

Alumno1["Sexo"] = "Masculino"
print(Alumno1)

# 5 Usar el metodo pop() para remover la edad del alumno, mostrar el diccionario completo.

Alumno1.pop("Sexo")

print(Alumno1)
# 6 Crear un diccionario que contenga las notas de un alumno en tres materias. Programacion 1 prog 2 y ciencia de datos.

Notas={"Programacion 1": "9","Ciencia de datos":"8","Programacion 2":"8"}

print("Las notas de",Alumno1.get("Nombre"),"son",Notas)
# 7 mostrar todos los items del diccionario de notas.

print(Notas.values())

# 8 Cear un nuevo diccionario que sea una copia del diccionario de notas del alumno. mostrar los datos del nuevo diccionario.

NuevoDiccionario=Notas.copy()
print(NuevoDiccionario)
print(Notas)

# 9 Mostrar los valores del diccionario de notas.

print(Notas.keys())

# 10 Mostrar la longitud del diccionario de notas.

print(len(Notas))