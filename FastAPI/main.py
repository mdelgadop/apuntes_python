from fastapi import FastAPI
from pydantic import BaseModel #para la validación de datos: pip install pydantic
from typing import Optional #para tener parámetros opcionales

class Libro(BaseModel):
    Titulo: str
    Autor:str
    Paginas:int
    Editorial:Optional[str]
 
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hola Mario"}


@app.get("/libros/{id}")
def mostrar_libro(id:int):
    return {"data" : id}

@app.post("/libros")
def insertar_libro(libro:Libro):
    return {"message" : f"libro {libro.Titulo} ha sido insertado" }
    