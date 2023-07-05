from fastapi import FastAPI
import uvicorn
import random
app = FastAPI()

@app.get("/")
def greet():
    return {"welcome" : "tetraplex"}

@app.get("/get_randomnum")
def get_randomnum():
    return {"random number is": random.randint(0,100)}

if __name__== "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")