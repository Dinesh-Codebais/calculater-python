from fastapi import FastAPI

app = FastAPI()

# Fake Database
calculations = []

# CREATE
@app.post("/add")
def add(num1: int, num2: int):

    result = num1 + num2

    data = {
        "id": 1,
        "calculation": f"{num1} + {num2}",
        "result": result
    }

    calculations.append(data)

    return {
        "message": "Calculation Added",
        "data": data
    }

# READ
@app.get("/calculations")
def get_calculations():

    return calculations

# UPDATE
@app.put("/update")
def update_calculation():

    calculations[0]["result"] = 100

    return {
        "message": "Calculation Updated",
        "data": calculations
    }

# DELETE
@app.delete("/delete")
def delete_calculation():

    calculations.pop()

    return {
        "message": "Calculation Deleted"
    }