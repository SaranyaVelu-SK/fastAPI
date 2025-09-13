from fastapi import FastAPI
from . import schema
app=FastAPI()

@app.post('/blog')
def postBlog(request:schema.Blog):
    return request