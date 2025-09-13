1. create a virtual environment
    **python -m venv myenv**
2. activate myenv by :
    **myenv -> Scripts -> select Activate.ps1  -> copy the file  path -> run it in terminal**
3. to deactivate
    **deactivate**
4. server needed for fastapi
    that server is - **uvicorn**
5. To install the required packages, run
    **pip3 install -r requirements.txt**
    (pip3 install -r Blog/requirements.txt)
6. to see all installed packages
    **pip list**
7. To run the main.py in the Blog folder
    **uvicorn Blog.main:app --reload**

------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## path parameters:
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


## Query parameters:
    Query parameters are values passed in the URL after ?, separated by &.

Example:

```python
@app.get('/blog/{id}')
def index(id:int, limit:int,published:Optional[bool]):
    return {
        "id":id,
        "limit":limit,
        "published":published
    }



/blog/99?limit=10&published=true


```

- id → Path parameter (/blog/{id} part)
- limit, published → Query parameters (after ?)
- Query parameters are not part of the path; they are extra key-value pairs that modify or filter the request.

#### How to Access Them in Function
You simply define them as function arguments:
```python
@app.get("/blog/{id}")
def index(id: int, limit: int, published: bool):
    return {"id": id, "limit": limit, "published": published}
```

- id → automatically taken from path /blog/{id}.
- limit, published → automatically read from query string.

*Example Request:*
*/blog/5?limit=20&published=true*
*Response:*
*{"id": 5, "limit": 20, "published": true}*

#### Role of Optional

Optional[X] = Union[X, None].

It means the parameter can either be of type X or None.

```python
from typing import Optional

def index(published: Optional[bool]):
    ...
```
**This does not by itself make the parameter optional in FastAPI. It only changes the type hint to accept None.**

#### What Happens If No Default Value Is Given?

If you write:
    published: Optional[bool]

FastAPI says:
    This parameter is required, but it may be bool or None.

Example:
Request /blog/99?limit=34 →  Error:

```python
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "published"],
      "msg": "Field required",
      "input": null
    }
  ]
}
```
If you write:
    published: Optional[bool] = None
FastAPI says:
    This parameter is truly optional, and if it’s not given, it defaults to None.

*Example:*
Request /blog/99?limit=34 → 
```python
{"id": 99, "limit": 34, "published": null}
```