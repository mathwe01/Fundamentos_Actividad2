from main import (validar_codigo, validar_texto_obligatorio, validar_tipo_consulta, asignar_prioridad)
LONGITUD_MINIMA = 8

def probar(nombre, obtenido, esperando):
    resultado = "CUMPLE" if obtenido == esperando else "NO CUMPLE"
    print(f"{nombre}: esperando: {esperando}, obtenido: {obtenido} => {resultado}")
    
print("== Pruebas ==")
probar("Datos validos (codigo)", validar_codigo("12345678", LONGITUD_MINIMA), True)
probar("Código vacío", validar_codigo("", LONGITUD_MINIMA), False)
probar("Tipo incorrecto", validar_tipo_consulta("comida"), False)
probar("Prioridad alta(pagos)", asignar_prioridad("pagos"), "Alta")
probar("Prioridad baja(constancia)", asignar_prioridad("constancia"), "Baja")