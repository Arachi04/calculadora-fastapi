from schemas import OperacionEnum

def suma(a:float, b:float) -> float:
    return a + b

def resta(a:float, b:float) -> float:
    return a - b

def multiplicacion(a:float, b:float) -> float:
    return a * b

def division(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    
    return a / b

# Diccionario de operaciones
OPERACIONES = {
    OperacionEnum.suma: suma,
    OperacionEnum.resta: resta,
    OperacionEnum.multiplicacion: multiplicacion,
    OperacionEnum.division: division
}

def calcular_operacion(a: float, b:float, operacion: OperacionEnum) -> float:
    funcion = OPERACIONES.get(operacion)
    if not funcion:
        raise ValueError("Operacion no soportada")
    
    return funcion(a, b)