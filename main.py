print("hello")

# from fastapi import FastAPI
# from typing import Optional

# app=FastAPI()

# @app.get('/')
# def greet():
#     return "Hellloooooo"

# # @app.get('/blog/{id}')
# # def index(id:int):
# #     return {'data':id}

# @app.get('/blog/{id}')
# def index(id:int, limit:int,published:Optional[bool]):
#     return {
#         "id":id,
#         "limit":limit,
#         "published":published
#     }


import sys
import gc

print("=== STEP 1: Reference counting demo ===")
a = [1, 2, 3]
print(f"Created list {a}, refcount =", sys.getrefcount(a))

b = a
print("Assigned b = a, refcount =", sys.getrefcount(a))

del b
print("Deleted b, refcount =", sys.getrefcount(a))

del a
print("Deleted a. Refcount is now 0 → List object destroyed.\n")


print("=== STEP 2: Cycle that reference counting cannot fix ===")

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None
    def __del__(self):
        print(f"Node {self.name} is being destroyed")

a = Node("A")
b = Node("B")
a.other = b
b.other = a

print("Created cycle: A ↔ B")
del a
del b
print("Deleted outside refs, but objects are STILL in memory (cycle alive).\n")


print("=== STEP 3: Forcing Garbage Collection ===")
unreachable = gc.collect()
print(f"Garbage collector ran and freed {unreachable} objects")
print("Now the cycle is gone.")