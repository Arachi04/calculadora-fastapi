from schemas import OperacionEnum

def calcular_operacion(a: float, b:float, operacion: OperacionEnum) -> float:
    if operacion == OperacionEnum.suma:
        return a + b
    elif operacion == OperacionEnum.resta:
        return a - b
    elif operacion == OperacionEnum.multiplicacion:
        return a * b
    elif operacion == OperacionEnum.division:
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b