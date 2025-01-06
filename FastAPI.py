from fastapi import FastAPI
app = FastAPI() #to store it in a variable
@app.get("/")
def chat():
    return {
       "name": "Emaan"
    }