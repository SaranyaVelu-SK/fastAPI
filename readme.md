1. create a virtual environment


**python -m venv myenv**


2. activate myenv by :

myenv -> Scripts -> select Activate.ps1  -> copy the file  path -> run it in terminal

3. to deactivate
**deactivate**

4. server needed for fastapi
- that server is - **uvicorn**

5. to see all installed packages
- pip list

---

## path parametere:
- to make dynamic routing, give the dynamic queries inside parantheses{}
- like :id in js, use {id} in python
- ex: 
```python
@app.get('/blog/{id}')
def index(id: int):
    return {'data':id}
    
```

#### Request:
GET /blog/42

#### Flow:
1. app.get('/blog/{id}') → returns decorator
2. decorator stores function `index` with path '/blog/{id}' in registry
3. Client sends GET /blog/42
4. FastAPI matches route pattern '/blog/{id}'
5. Extracts id = '42'
6. Sees function signature expects id: int → converts '42' → 42
7. Calls index(42)
8. index returns {'data': 42}
9. FastAPI turns dict into JSON
10. Uvicorn sends JSON response {"data": 42}