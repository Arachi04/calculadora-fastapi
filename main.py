from fastapi import FastAPI, HTTPException
from schemas import OperacionRequest
from services import calcular_operacion

app = FastAPI(title="Calculadora con Services")

@app.post("/calcular")
def calcular(datos: OperacionRequest):
    try:
        resultado = calcular_operacion(
            a = datos.a, 
            b = datos.b, 
            operacion = datos.operacion
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400, 
            detail = str(error)
        )
    
    return{
        "a": datos.a,
        "b": datos.b,
        "operacion": datos.operacion,
        "resultado": resultado
    }

@app.get("/")
def home():
    return {"mensaje" : "API de calculadora activa"}