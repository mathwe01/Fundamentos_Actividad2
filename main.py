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

def main():
    opcion = ""
    while opcion != "3":
        mostrar_menu()
        opcion = input("Elija una opción: ")

main()