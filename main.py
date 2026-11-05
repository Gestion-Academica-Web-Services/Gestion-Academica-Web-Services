from fastapi import FastAPI

app = FastAPI(title="Gestión Académica API")

@app.get("/")
def read_root():
    return {"mensaje": "El servidor está corriendo perfectamente"}