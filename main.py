from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

# Table Create
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Database Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



# CREATE
@app.post("/add")
def add(num1: int, num2: int):

    result = num1 + num2

<<<<<<< HEAD
    db = SessionLocal()
=======
    data = {
        "id": len(calculations) + 1,
        "calculation": f"{num1} + {num2}",
        "result": result
    }
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a

    new_calculation = models.Calculation(
        calculation=f"{num1} + {num2}",
        result=str(result)
    )

    db.add(new_calculation)

    db.commit()

    db.refresh(new_calculation)

    db.close()

    return {
        "message": "Calculation Added",
        "data": {
            "id": new_calculation.id,
            "calculation": new_calculation.calculation,
            "result": new_calculation.result
        }
    }

<<<<<<< HEAD

=======
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a
# READ ALL
@app.get("/calculations")
def get_calculations():

    db = SessionLocal()

    calculations = db.query(models.Calculation).all()

    db.close()

    return calculations


# READ SINGLE
@app.get("/calculation/{id}")
def get_single_calculation(id: int):

<<<<<<< HEAD
    db = SessionLocal()

    calculation = db.query(models.Calculation).filter(
        models.Calculation.id == id
    ).first()

    db.close()

    if calculation:

        return calculation
=======
    for calc in calculations:

        if calc["id"] == id:

            return calc
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a

    return {
        "message": "Calculation Not Found"
    }


<<<<<<< HEAD
# DELETE
@app.delete("/delete/{id}")
def delete_calculation(id: int):

    db = SessionLocal()

    calculation = db.query(models.Calculation).filter(
        models.Calculation.id == id
    ).first()

    if calculation:

        db.delete(calculation)

        db.commit()

        db.close()

        return {
            "message": "Calculation Deleted"
        }

    db.close()
=======
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
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a

    return {
        "message": "Calculation Not Found"
    }

<<<<<<< HEAD
# SUBTRACT
=======

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
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a
@app.post("/subtract")
def subtract(num1: int, num2: int):

    result = num1 - num2

<<<<<<< HEAD
    db = SessionLocal()

    new_calculation = models.Calculation(
        calculation=f"{num1} - {num2}",
        result=str(result)
    )

    db.add(new_calculation)

    db.commit()

    db.refresh(new_calculation)

    db.close()

    return {
        "message": "Subtraction Added",
        "data": new_calculation
    }

# MULTIPLY
=======
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
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a
@app.post("/multiply")
def multiply(num1: int, num2: int):

    result = num1 * num2

<<<<<<< HEAD
    db = SessionLocal()

    new_calculation = models.Calculation(
        calculation=f"{num1} * {num2}",
        result=str(result)
    )

    db.add(new_calculation)

    db.commit()

    db.refresh(new_calculation)

    db.close()

    return {
        "message": "Multiplication Added",
        "data": new_calculation
    }

# DIVIDE
=======
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
>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a
@app.post("/divide")
def divide(num1: int, num2: int):

    if num2 == 0:

        return {
            "message": "Cannot divide by zero"
        }

    result = num1 / num2

<<<<<<< HEAD
    db = SessionLocal()

    new_calculation = models.Calculation(
        calculation=f"{num1} / {num2}",
        result=str(result)
    )

    db.add(new_calculation)

    db.commit()

    db.refresh(new_calculation)

    db.close()

    return {
        "message": "Division Added",
        "data": new_calculation
    }

# UPDATE
@app.put("/update/{id}")
def update_calculation(id: int, num1: int, num2: int):

    db = SessionLocal()

    calculation = db.query(models.Calculation).filter(
        models.Calculation.id == id
    ).first()

    if calculation:

        calculation.calculation = f"{num1} + {num2}"

        calculation.result = str(num1 + num2)

        db.commit()

        db.refresh(calculation)

        db.close()

        return {
            "message": "Calculation Updated",
            "data": calculation
        }

    db.close()

    return {
        "message": "Calculation Not Found"
    }
=======
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

>>>>>>> d77ee8deaf5fa9272f4e0f0e409e3696e65f575a
