# Sintaxis Básica de Julia para Programación Matemática y Cálculo Numérico

¡Bienvenidos! Este repositorio contiene los conceptos esenciales de Julia explicados de manera sencilla, con ejemplos prácticos y un enfoque en aplicaciones numéricas. Cada sección incluye una descripción detallada y código ejecutable.

## Tabla de Contenidos

1. [Formateo de Salida por Consola](#formateo-de-salida-por-consola)
2. [Operadores Aritméticos y Lógicos](#operadores-aritméticos-y-lógicos)
3. [Variables y Tipos de Datos](#variables-y-tipos-de-datos)
4. [Estructuras de Control](#estructuras-de-control)
5. [Funciones](#funciones)
6. [Estructuras de Datos](#estructuras-de-datos)
7. [Manejo de Archivos](#manejo-de-archivos)
8. [Bucles y Comprensiones](#bucles-y-comprensiones)
9. [Manejo de Errores](#manejo-de-errores)
10. [Paquetes y Módulos](#paquetes-y-módulos)
11. [Mejores Prácticas](#mejores-prácticas)
12. [Tipos especiales](tipos-especiales)
13. [Interpolación Básica](#interpolación-básica)
14. [Concatenación](#concatenación)

---

## Formateo de Salida por Consola

**Descripción:** Julia permite formatear salidas usando `println`, interpolación de strings (`$`) y la macro `@printf` (del paquete `Printf`) para controlar decimales y alineación.

**Ejemplo:**

```julia
using Printf
nombre = "Ana"
edad = 25
temperatura = 36.5

# Interpolación básica
println("Hola, $nombre. Tienes $edad años.")

# Formateo numérico con @printf
@printf("Temperatura: %.2f°C\n", temperatura)  # Salida: Temperatura: 36.50°C
```

##Operadores Aritméticos y Lógicos
**Concepto**
Son aquellas operaciones que vienen integradas en el lenguaje para hacer operaciones básicas como la suma, resta, multiplicación y división, exponenciación , resto, entre otras y además nos ayudan también a la hora de evaluar condiciones que son determinantes para obtener resultados de comparaciones de 1 o más condiciones en cadena y estas son usadas en las estructuras condicionales.

```julia
#Operdores Aritméticos
suma = 5 + 3       # Suma
resta = 10 - 4     # Resta
multiplicacion = 6 * 7 # Multiplicación
division = 8 / 2   # División
modulo = 10 % 3    # Módulo (resto de la división)
potencia = 2 ^ 3   # Potencia

#Operdores Lógicos
and_logico = true && false  # AND lógico
or_logico = true || false   # OR lógico
not_logico = !true
```

##Variables y Tipos de Datos
**Concepto de Variable**  
Mecanismo para almacenar y manipular datos. Julia usa asignación dinámica con tipado fuerte pero flexible, permitiendo reutilizar nombres de variables con distintos tipos (aunque no recomendado para optimización).
**Concepto de Tipo de Dato**  
Clasificaciones que determinan cómo se almacenan y operan los valores en memoria. Julia implementa tipos primitivos y compuestos con múltiples niveles de abstracción.

```julia
x = 42                   # Int
y::Float64 = 3.14        # Float64 explícito
nombre = "Julia"         # String
es_activo = true         # Bool
caracter = 'J'           # Char

println("Tipo de x: ", typeof(x))  # Salida: Tipo de x: Int64
```

##Estructuras de Control
**Concepto:**  
Flujos de ejecución condicionales e iterativos que permiten implementar lógica compleja mediante bifurcaciones y repeticiones.

```julia
# Condicional
nota = 85
if nota >= 90
    println("A")
elseif nota >= 80
    println("B")  # Salida: B
else
    println("C")
end

# Bucle for
for i in 1:3
    println("Iteración $i")  # Salida: Iteración 1, 2, 3
end

```

##Funciones
**Concepto:**  
Bloques reusables de código con despacho múltiple, donde la versión específica a ejecutar se selecciona basada en los tipos de los argumentos.

Descripción: Se definen con function. Julia permite argumentos opcionales y múltiples dispatch.

```julia
# Función básica
function suma(a, b=0)  # b es opcional (default 0)
    return a + b
end

println(suma(3, 4))   # 7
println(suma(5))      # 5

```

##Estructuras de Datos
**Concepto:**  
Estructuras multidimensionales para almacenamiento eficiente de datos numéricos, con sintaxis unificada para álgebra lineal y operaciones elemento a elemento.
Visto desde otro punto es una forma de organizar y almacenar datos como listas (arrays), pares clave-valor (diccionarios) o colecciones inmutables (tuplas).

```julia
# Array
numeros = [1, 2, 3]
push!(numeros, 4)  # [1, 2, 3, 4]

# Diccionario
estudiante = Dict("nombre" => "Luisa", "edad" => 22)
println(estudiante["nombre"])  # Luisa

```

##Manejo de Archivos
**Concepto:**  
Protocolos para comunicación con dispositivos externos y persistencia de datos, implementando buffers y acceso concurrente seguro.
Son de las mejores Operaciones para leer y escribir datos en archivos externos, esencial para trabajar con datasets o guardar resultados.
Descripción: Lectura/escritura con open, read, y write.

```julia
# Escritura
open("datos.txt", "w") do archivo
    write(archivo, "Hola, Julia\n")
end

# Lectura
contenido = open("datos.txt") do archivo
    read(archivo, String)
end
println(contenido)  # Hola, Julia

```

##Bucles y Comprensiones
Concepto: Técnicas para crear colecciones (como arrays) de forma compacta o iterar sobre elementos con lógica embebida.
Descripción: Comprensiones de colecciones para crear arrays de forma concisa.

```julia
cuadrados = [i^2 for i in 1:5]  # [1, 4, 9, 16, 25]
```

##Manejo de Errores
Concepto: Mecanismos para detectar y gestionar fallos en tiempo de ejecución, evitando que el programa se detenga abruptamente.
Descripción: Uso de try-catch para manejar excepciones.

```julia

    try
    sqrt(-1)
catch e
    println("Error: ", e)  # Error: DomainError...
end

```

##Paquetes y Módulos
Concepto: Conjuntos de código organizado que amplían las funcionalidades base de Julia, como herramientas para álgebra lineal o visualización.
Descripción: Instalación y uso de paquetes con ] add NombrePaquete.

```julia
using LinearAlgebra
A = [1 2; 3 4]
println(det(A))  # -2.0
```

**Mejores prácticas:**

- Usar nombres descriptivos (`temp_max` vs `t1`) [6]
- Letras griegas permitidas: `δ = 0.01` (teclear `\delta` + Tab en REPL)

**Tipos especiales:**  
`NaN`, `Inf` (para operaciones no numéricas) [3]

## Manipulación de Strings

**Concepto:**  
Herramientas para creación, interpolación y procesamiento de cadenas de texto, incluyendo operaciones vectorizadas y formatos personalizados.
##Interpolación y operaciones

```julia
saludo = "Hola $nombre, tienes $(edad+1) años próximamente."
```

##Concatenación

```julia
str1 = "Julia es " * "potente" * " para cálculos." # Usar * en vez de +
```
