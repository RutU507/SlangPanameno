import sqlite3

# Función para crear la tabla en la base de datos si no existe
def crear_tabla():
    conn.execute('''CREATE TABLE IF NOT EXISTS slang (
                    palabra TEXT PRIMARY KEY,
                    significado TEXT NOT NULL)''')

# Función para agregar una nueva palabra al diccionario
def agregar_palabra():
    palabra = input("Ingrese la palabra en slang panameño: ")
    significado = input("Ingrese el significado de la palabra: ")
    conn.execute("INSERT INTO slang (palabra, significado) VALUES (?, ?)", (palabra, significado))
    conn.commit()
    print("Palabra agregada exitosamente.")

# Función para editar el significado de una palabra existente
def editar_palabra():
    palabra = input("Ingrese la palabra en slang panameño que desea editar: ")
    nuevo_significado = input("Ingrese el nuevo significado de la palabra: ")
    conn.execute("UPDATE slang SET significado = ? WHERE palabra = ?", (nuevo_significado, palabra))
    conn.commit()
    print("Palabra editada exitosamente.")

# Función para eliminar una palabra existente
def eliminar_palabra():
    palabra = input("Ingrese la palabra en slang panameño que desea eliminar: ")
    conn.execute("DELETE FROM slang WHERE palabra = ?", (palabra,))
    conn.commit()
    print("Palabra eliminada exitosamente.")

# Función para mostrar todas las palabras del diccionario
def ver_listado_palabras():
    cursor = conn.execute("SELECT palabra, significado FROM slang")
    for row in cursor:
        print("Palabra:", row[0])
        print("--------------------")

# Función para buscar el significado de una palabra
def buscar_significado():
    palabra = input("Ingrese la palabra en slang panameño que desea buscar: ")
    cursor = conn.execute("SELECT significado FROM slang WHERE palabra = ?", (palabra,))
    row = cursor.fetchone()
    if row is not None:
        print("El significado de la palabra '{}' es: {}".format(palabra, row[0]))
    else:
        print("La palabra '{}' no se encontró en el diccionario.".format(palabra))

# Conexión a la base de datos
conn = sqlite3.connect('slang_panameno.db')

# Crear la tabla si no existe
crear_tabla()

# Agregar palabras predeterminadas a la base de datos
conn.execute("INSERT INTO slang (palabra, significado) VALUES (?, ?)",
             ("Mopri", " Es primo y no solo se refiere al hijo del tío de una persona como dice la RAE, sino que también describe a un amigo o pasiero."))
conn.execute("INSERT INTO slang (palabra, significado) VALUES (?, ?)",
             ("Llesca", "Es lugar de la calle."))
conn.execute("INSERT INTO slang (palabra, significado) VALUES (?, ?)",
             ("¡Chuzo!", "Es una interjección que utilizamos para verbalizar algún sentimiento o impresión."))
conn.execute("INSERT INTO slang (palabra, significado) VALUES (?, ?)",
             ("Compa", "Es una abreviación de la palabra compadre y se utiliza, especialmente entre hombres, bien para referirse a un amigo o entre desconocidos pero buscando dar un trato afable y cortés a la vez."))
conn.execute("INSERT INTO slang (palabra, significado) VALUES (?, ?)",
             ("xopa", "es el argot de Panamá equivalente a decir ¿qué pasa"))
# Menú principal de la aplicación
while True:
    print("\n*** Diccionario de Slang Panameño ***")
    print("Seleccione una opción:")
    print("a) Agregar nueva palabra")
    print("c) Editar palabra existente")
    print("d) Eliminar palabra existente")
    print("e) Ver listado de palabras")
    print("f) Buscar significado de palabra")
    print("g) Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion.lower() == 'a':
        agregar_palabra()
    elif opcion.lower() == 'c':
        editar_palabra()
    elif opcion.lower() == 'd':
        eliminar_palabra()
    elif opcion.lower() == 'e':
        ver_listado_palabras()
    elif opcion.lower() == 'f':
        buscar_significado()
    elif opcion.lower() == 'g':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# Cerrar la conexión a la base de datos
conn.close()
