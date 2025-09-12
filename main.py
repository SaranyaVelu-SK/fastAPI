print("hello")

from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def greet():
    return "Hellloooooo"

@app.get('/blog/{id}')
def index(id:int):
    return {'data':id}