from fastapi import FastAPI

app = FastAPI()

# Fake Database
calculations = []


# CREATE
@app.post("/add")
def add(num1: int, num2: int):

    result = num1 + num2

    data = {
        "id": len(calculations) + 1,
        "calculation": f"{num1} + {num2}",
        "result": result
    }

    calculations.append(data)

    return {
        "message": "Calculation Added",
        "data": data
    }

# READ ALL
@app.get("/calculations")
def get_calculations():

    return calculations


# READ SINGLE
@app.get("/calculation/{id}")
def get_single_calculation(id: int):

    for calc in calculations:

        if calc["id"] == id:

            return calc

    return {
        "message": "Calculation Not Found"
    }


# UPDATE
@app.put("/update/{id}")
def update_calculation(id: int, num1: int, num2: int):

    for calc in calculations:

        if calc["id"] == id:

            calc["calculation"] = f"{num1} + {num2}"

            calc["result"] = num1 + num2

            return {
                "message": "Calculation Updated",
                "data": calc
            }

    return {
        "message": "Calculation Not Found"
    }


# DELETE
@app.delete("/delete/{id}")
def delete_calculation(id: int):

    for calc in calculations:

        if calc["id"] == id:

            calculations.remove(calc)

            return {
                "message": "Calculation Deleted"
            }

    return {
        "message": "Calculation Not Found"
    }

# SUBTRACTION
@app.post("/subtract")
def subtract(num1: int, num2: int):

    result = num1 - num2

    data = {
        "id": len(calculations) + 1,
        "calculation": f"{num1} - {num2}",
        "result": result
    }

    calculations.append(data)

    return {
        "message": "Subtraction Added",
        "data": data
    }

# MULTIPLICATION
@app.post("/multiply")
def multiply(num1: int, num2: int):

    result = num1 * num2

    data = {
        "id": len(calculations) + 1,
        "calculation": f"{num1} * {num2}",
        "result": result
    }

    calculations.append(data)

    return {
        "message": "Multiplication Added",
        "data": data
    }

# DIVISION
@app.post("/divide")
def divide(num1: int, num2: int):

    if num2 == 0:

        return {
            "message": "Cannot divide by zero"
        }

    result = num1 / num2

    data = {
        "id": len(calculations) + 1,
        "calculation": f"{num1} / {num2}",
        "result": result
    }

    calculations.append(data)

    return {
        "message": "Division Added",
        "data": data
    }

