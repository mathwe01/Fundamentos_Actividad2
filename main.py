#Sistema de Orientación y registro de atenciones para el módulo de soporte academico
def mostrar_menu():
    # Solo imprime las opciones, no recibe nada ni devuelve nada
    print("\n=== SOPORTE ACADÉMICO ===")
    print("1. Registrar solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")

def validar_texto_obligatorio(texto):
    # Recibe un texto y me dice si tiene algo escrito o está vacío
    limpio = texto.strip()  # variable local, solo existe dentro de esta función
    return limpio != ""

def validar_codigo(codigo, longitud_minima):
    # Recibo el codigo y la longitud mínima como parámetros para no usar variables globales
    limpio = codigo.strip()
    return limpio != "" and len(limpio) >= longitud_minima

def validar_tipo_consulta(tipo):
    # Recibe el tipo de consulta que escribió el usuario y revisa si está en la lista permitida
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]  # variable local, la lista solo se usa aquí
    return tipo.strip().lower() in tipos_validos

def asignar_prioridad(tipo):
    # Segun el tipo de consulta que reciba, devuelve si la prioridad es alta, media o baja

    tipo=tipo.strip().lower()
    if tipo in ["matricula", "pagos"]:
        prioridad = "Alta"  # variable local, solo se usa dentro de esta función
    elif tipo == "plataforma":
        prioridad = "Media"
    else:
        prioridad = "Baja"
    return prioridad

def registrar_solicitud(codigo, nombre, tipo, descripcion, prioridad):
    # Recibe todos los datos por parámetros y los junta en un diccionario
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo.strip(),
        "descripcion": descripcion.strip(),
        "prioridad": prioridad,
    }  # variable local, la devuelvo con return para usarla en main
    return solicitud

def mostrar_resumen(solicitud):
    # Recibe una solicitud y la muestra en pantalla, no devuelve nada
    print("\n=== Resumen de la solicitud ===")
    print("Código:", solicitud["codigo"])
    print("Nombre:", solicitud["nombre"])
    print("Tipo de consulta:", solicitud["tipo"])
    print("Descripción:", solicitud["descripcion"])
    print("Prioridad:", solicitud["prioridad"])
        
    
def main():
    # Estas variables son del programa principal y solo existen dentro de main
   LONGITUD_MINIMA = 8
   opcion = ""
   solicitudes = []
   while opcion != "3":
       mostrar_menu()
       opcion = input("Elija una opcion: ")
       
       if opcion == "1":
           codigo = input("Código de estudiante: ")
           nombre = input("Nombre : ")
           print("Tipos de consulta: matricula, pagos, constancia, plataforma, otro")
           tipo = input("Tipo de consulta: ")
           descripcion = input("Descripción breve: ")
       
           if not validar_codigo(codigo, LONGITUD_MINIMA):
               print("Error: el código debe tener al menos 8 caracteres.")
           elif not validar_texto_obligatorio(nombre) or not validar_texto_obligatorio(descripcion):
               print("Error: el nombre y la descripción son obligatorios.")
           elif not validar_tipo_consulta(tipo):
               print("Error: tipo de consulta inválido.")
           else:
               prioridad = asignar_prioridad(tipo)
               solicitud = registrar_solicitud(codigo, nombre, tipo, descripcion, prioridad)
               solicitudes.append(solicitud)
               mostrar_resumen(solicitud)
               
       elif opcion == "2":
            if len(solicitudes) == 0:
                print("Aún no hay solicitudes registradas.")
            else:
                print("\nTotal de solicitudes:", len(solicitudes))
                for solicitud in solicitudes:
                    mostrar_resumen(solicitud)
                
main()