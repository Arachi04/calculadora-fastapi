from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI(title="API Calculadora con Enum")

# 1. Enum de operaciones permitidas
class OperacionEnum(str, Enum):
    suma = "suma"
    resta = "resta"
    multiplicacion = "multiplicacion"
    division = "division"

# . Modelo de datos (body)
class OperacionRequest(BaseModel):
    a: float
    b: float
    operacion: OperacionEnum

# . Endpoint POST
@app.post("/calcular")
def calcular(datos: OperacionRequest):
    if datos.operacion == OperacionEnum.suma:
        resultado = datos.a + datos.b

    elif datos.operacion == OperacionEnum.resta:
        resultado = datos.a - datos.b

    elif datos.operacion == OperacionEnum.multiplicacion:
        resultado = datos.a * datos.b

    elif datos.operacion == OperacionEnum.division:
        if datos.b == 0:
            raise HTTPException(
                status_code=400, 
                detail="No se puede dividir entre cero"
                )
        resultado = datos.a / datos.b
        
    return{
        "a": datos.a,
        "b": datos.b,
        "operacion": datos.operacion,
        "resultado": resultado
    }


@app.get("/")
def home():
    return {"mensaje" : "API de calculadora activa"}