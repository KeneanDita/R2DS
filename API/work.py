from fastapi import FastAPI

app = FastAPI()

inventory = {
    1:{
        "name": "Milk",
        "price": 3.99,
        "Brand": "Mike"
    }
}

@app.get("/get-item/{item_id}")

def get_item(item_id: int):
    return inventory[item_id]