from fastapi import FastAPI
from stock import *
from pydantic import BaseModel
import uvicorn

class Requette(BaseModel):
    sujet:str


# instanciation de L'API
app = FastAPI()
@app.get("/")

def requette():
    return save_subject_data("biden")

if __name__ == "__main__":

    uvicorn.run(app)