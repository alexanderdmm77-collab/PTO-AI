from fastapi import FastAPI

app = FastAPI(title="ПТО.ИИ")

@app.get("/")
def root():
    return {
        "project": "ПТО.ИИ",
        "status": "Работает"
