#Sistema de Orientación y registro de atenciones para el módulo de soporte academico
def mostrar_menu():
    print("\n=== SOPORTE ACADÉMICO ===")
    print("1. Registrar solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")

def validar_texto_obligatorio(texto):
    limpio = texto.strip()
    return limpio != ""

def validar_codigo(codigo, longitud_minima):
    limpio = codigo.strip()
    return limpio != "" and len(limpio) >= longitud_minima

def validar_tipo_consulta(tipo):
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    return tipo.strip().lower() in tipos_validos

def asignar_prioridad(tipo):
    tipo=tipo.strip().lower()
    if tipo in ["matricula", "pagos"]:
        prioridad = "Alta"
    elif tipo == "plataforma":
        prioridad = "Media"
    else:
        prioridad = "Baja"
    return prioridad

def registrar_solicitud(codigo, nombre, tipo, descripcion, prioridad):
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo.strip(),
        "descripcion": descripcion.strip(),
        "prioridad": prioridad,
    }
    return solicitud

def mostrar_resumen(solicitud):
    print("\n=== Resumen de la solicitud ===")
    print("Código:", solicitud["codigo"])
    print("Nombre:", solicitud["nombre"])
    print("Tipo de consulta:", solicitud["tipo"])
    print("Descripción:", solicitud["descripcion"])
    print("Prioridad:", solicitud["prioridad"])
        
    
def main():
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