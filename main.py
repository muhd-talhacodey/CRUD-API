# Creating a basic API for now 
# Uvicorn is a small web server which is used to communicate with the browser in real-time

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {
        "name" : "John da don", 
        "age" : 41, 
        "message" : "I am here for a mission", 
    }