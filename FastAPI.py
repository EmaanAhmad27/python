# from fastapi import FastAPI
# from langchain_google_genai import GoogleGenerativeAI
# from dotenv import load_dotenv
# import os
# load_dotenv()
# app = FastAPI()
# llm = GoogleGenerativeAI(model = "gemini-1.5-flash", api_key = os.getenv("GoogleAPIKey"))
# @app.get("/chat")
# def chat (query:str):
#    prompt = "you are a tutor of programming userquery:"
#    result= llm.invoke(prompt + query)
#    return {result}
#/docs is needed after the port name to get the answer.
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def chat ():
   return {"emaan"}

# @app.get("/auth/{id}")
# def login (id):
#    print(id)
#    return {"function is calling"}

# @app.get("/auth/register")
# def register (val, username, count):
#    print(val, username, count)
#    return val, username, count


from typing import Union

@app.get("/auth/register")
def register (val:int, username:str, count:int | None = None):
   print(val, username, count)
   return val, username, count
# from pydantic import BaseModel

# class User(BaseModel): #this will be our dictionary which has variable and data type of our choice
#    name: Optional[str] #this parameter is optional but if it is passed my user it is string.
#    age: int














