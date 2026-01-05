from fastapi import FastAPI, HTTPException
from schemas import OperacionEnum, OperacionRequest

app = FastAPI(title="API Calculadora con Schemas")

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