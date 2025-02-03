from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


# Modelo de datos para el cuerpo de la petición
class Item(BaseModel):
    nombre: str
    precio: float
@app.get("/")
def read_root():
    return {"message": "¡Hola, API funcionando!"}

@app.get("/saludo/{nombre}")  # Endpoint con parámetro
def saludar(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}

@app.post("/items/")
def crear_item(item: Item):
    return {"item": item.nombre, "precio": item.precio}