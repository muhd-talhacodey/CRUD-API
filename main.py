<<<<<<< HEAD
=======
# CRUD API
"""
Fast API ----> Is the Library we will use to create the API 
Uvicorn ----> It is a small web server to which the browser communicates... 
Pydantic imports strict data validation at run-time
/ --- It is the root meaning that when you enter a building for example it is the front-desk 
/status -- It is checking the uptime for the server or entering a specific room in the building

if you want to carry out asynch tasks apply this 
async def example() ----> Like this
"""
>>>>>>> cad9990b7f51b37156a2fde6e3c7c6bc6680bf03

<<<<<<< HEAD
=======

"""
Implemented a to-do list with all HTTP methods with Fast API
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

todo_list = ["Read a book", "Do chores" , "Study"]

app = FastAPI()

class Item(BaseModel):
    name : str 

# GET ---> Read the items already mentioned in the list
@app.get("/todo")
def todo_read():
    return{
        "List" : todo_list
    }

# POST ---> Create to add more tasks in the To Do List

@app.post("/todo/create")
def todo_create(todo_create: Item):
    todo_list.append(todo_create.name)
    return{
        "Successfully added" : todo_create.name , 
        "New List" : todo_list
    }


@app.delete("/delete")
def item_remove(delete_item: str):
    for item in food_items:
        if item == delete_item:
            food_items.remove(item)
        return{
            "New List" : food_items
        }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




>>>>>>> cad9990b7f51b37156a2fde6e3c7c6bc6680bf03
