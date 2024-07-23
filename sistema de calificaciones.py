# Variables
estudiantes =[]

# Funciones

def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
    try:
      num_estudiantes = int(input("\nIngrese el número de estudiantes a registrar:\n___"))
      
      return num_estudiantes
    except ValueError:
      print("""
      ========================================
      El valor ingresado no es una opción válida
      ========================================\n""")
    
def obtener_nombre_estudiante():
    # Pide al usuario el nombre del estudiante y devuelve el valor
    nombre_estudiante = input("\nIngrese nombre del estudiante:\n___")
    
    return nombre_estudiante

def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    try:
      numero_asignaturas = int(input("\nIngrese el número de asignaturas:\n___"))
      
      return numero_asignaturas
    
    except ValueError:
      print("""
      ========================================
      Por favor ingrese solo números 
      ========================================\n""")
    
def obtener_calificaciones(num_asignaturas):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    calificaciones = []
    
    for i in range(num_asignaturas):
      
      print(f"""
      \n Asignatura {i+1} de {num_asignaturas}\n\n""")
      
      try:
        nota = int(input("\nIngrese la nota:\n___"))
        
        if nota >= 0 and nota <= 10:
          calificaciones.append(nota)
        else:
          print("\nIngrese valores entre 0 y 10\n")
          break
        
      except ValueError:
        print('\nIngrese solo números\n')
        
    return calificaciones

def calcular_promedio(calificaciones):
    # Calcula y devuelve el promedio de las calificaciones
    return (sum(calificaciones))/len(calificaciones)

def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    if promedio >=6:
      return "Aprobado"
    else:
      return "Reprobado"

def imprimir_resumen(estudiantes):
    # Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    for estudiante in estudiantes:
      
      print(f"""
      =================================================
      Resumen del estudiante {estudiante["nombre"]}:
      
      Promedio: {estudiante["promedio"]}
      Estado: {estudiante["estado"]}
      """)
  
def inicio():
  
  print("\n Bienvenido al Sistema de Calificaciones \n")
  
  while True:
    
    try:
      option = int(input("""\nMENÚ
            
      Ingrese el número de la opción:
            
      1. Ingresar estudiantes
      2. Salir
      _____"""))
      
      if option == 2:
        break
      if option ==1:
        num_estudiantes = obtener_numero_estudiantes()
        
        for i in range(num_estudiantes):
          print(f"\nEstudiante {i+1} de {num_estudiantes}\n\n")
          
          nombre_estudiante = obtener_nombre_estudiante()
          num_asignaturas = obtener_numero_asignaturas()
          calificaciones = obtener_calificaciones(num_asignaturas)
          promedio = calcular_promedio(calificaciones)
          estado = determinar_estado(promedio)
          
          estudiantes.append({
            "nombre": nombre_estudiante,
            "promedio": promedio,
            "estado": estado
          })
          
        imprimir_resumen(estudiantes)
    except ValueError:
      print("""
      ========================================
      El valor ingresado no es una opción válida
      ========================================\n""")
    except:
      print("""
      ========================================
      Ocurrió algo extraño, intentalo nuevamente
      ========================================""")
      
inicio()      