import time
import random

# ==========================================
# CONFIGURACIÓN
# ==========================================

ALUMNOS = 100000
MATERIAS = 10000

ALUMNO_BUSCAR = 321
MATERIA_BUSCAR = 5


# ==========================================
# OPCIÓN 1:
# ALUMNOS = FILAS
# MATERIAS = COLUMNAS
# ==========================================

matriz_alumnos_filas = []

for alumno in range(ALUMNOS):
    fila = []

    for materia in range(MATERIAS):
        calificacion = random.randint(1, 10)
        fila.append(calificacion)

    matriz_alumnos_filas.append(fila)


# Buscar alumno 321, materia 5
inicio = time.perf_counter()

resultado1 = matriz_alumnos_filas[ALUMNO_BUSCAR - 1][MATERIA_BUSCAR - 1]

fin = time.perf_counter()

tiempo1 = fin - inicio


# ==========================================
# OPCIÓN 2:
# MATERIAS = FILAS
# ALUMNOS = COLUMNAS
# ==========================================

matriz_materias_filas = []

for materia in range(MATERIAS):
    fila = []

    for alumno in range(ALUMNOS):
        calificacion = random.randint(1, 10)
        fila.append(calificacion)

    matriz_materias_filas.append(fila)


# Buscar alumno 321, materia 5
inicio = time.perf_counter()

resultado2 = matriz_materias_filas[MATERIA_BUSCAR - 1][ALUMNO_BUSCAR - 1]

fin = time.perf_counter()

tiempo2 = fin - inicio


# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print("==========================================")
print("        RESULTADOS DE LA BÚSQUEDA")
print("==========================================")

print("\nALUMNOS EN FILAS / MATERIAS EN COLUMNAS")
print("Alumno:", ALUMNO_BUSCAR)
print("Materia:", MATERIA_BUSCAR)
print("Calificación:", resultado1)
print("Tiempo de búsqueda:", tiempo1, "segundos")


print("\nMATERIAS EN FILAS / ALUMNOS EN COLUMNAS")
print("Alumno:", ALUMNO_BUSCAR)
print("Materia:", MATERIA_BUSCAR)
print("Calificación:", resultado2)
print("Tiempo de búsqueda:", tiempo2, "segundos")


# ==========================================
# COMPARACIÓN
# ==========================================

print("\n==========================================")
print("              COMPARACIÓN")
print("==========================================")

if tiempo1 < tiempo2:
    print("La primera opción fue más rápida.")
    print("Alumnos en filas y materias en columnas.")

elif tiempo2 < tiempo1:
    print("La segunda opción fue más rápida.")
    print("Materias en filas y alumnos en columnas.")

else:
    print("Ambas opciones tuvieron el mismo tiempo.")