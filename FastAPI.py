from fastapi import FastAPI
from typing import Union, Optional
from pydantic import BaseModel

class User(BaseModel): #this will be our dictionary which has variable and data type of our choice
   name: Optional[str] #this parameter is optional but if it is passed my user it is string.
   age: int
app = FastAPI() #to store it in a variable
@app.get("/")
def chat():
    return {
       "name": "Emaan"
    }
@app.get("/auth/login")
def login():
   print("Login function calling")
   return ("Login function calling")

@app.get("/auth/register")
def register (username:User): #to add value directly
   return {"username":username}

# @app.get("/auth/register")
# def register (value:int,username:User,count:int | None = None): #to add value directly
#    print (value)
#    return {"value":value, "username":username, "count":count}

@app.get("/auth/{id}")
def login(id): 
   print(id)
   return ("Login function calling")






