from pydantic import BaseModel
from enum import Enum

# Enum de operaciones permitidas
class OperacionEnum(str, Enum):
    suma = "suma"
    resta = "resta"
    multiplicacion = "multiplicacion"
    division = "division"

# Modelo del body
class OperacionRequest(BaseModel):
    a: float
    b: float
    operacion: OperacionEnum