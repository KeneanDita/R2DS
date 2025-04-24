from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/about")
def about():
    return {"message": "about"}