#Sistema de Orientación y registro de atenciones para el módulo de soporte academico
def mostrar_menu():
    print("\n=== SOPORTE ACADÉMICO ===")
    print("1. Registrar solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")

def main():
    opcion = ""
    while opcion != "3":
        mostrar_menu()
        opcion = input("Elija una opción: ")


main()