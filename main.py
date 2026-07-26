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
Let's implement we are at the supermarket and we need to buy some items, implement CR on it... 
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

food_items = ["Milk", "Bread" , "Eggs"]

class Item(BaseModel):
    name : str

# GET ---> Read the items alr mentioned in the list 

@app.get("/")
def items_present():
    return{
        "food basket" : food_items
    }

# POST ---> Create to add more items in the basket 

@app.post("/items")
def item_added(new_item: Item):
    food_items.append(new_item.name)
    return{
        "status" : f"Successfully added {new_item.name}",
        "Updated Basket" : food_items
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