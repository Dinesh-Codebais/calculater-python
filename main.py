from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

# Create Tables
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

    db = SessionLocal()

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

    db = SessionLocal()

    calculation = db.query(models.Calculation).filter(
        models.Calculation.id == id
    ).first()

    db.close()

    if calculation:
        return calculation

    return {
        "message": "Calculation Not Found"
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

    return {
        "message": "Calculation Not Found"
    }


# SUBTRACTION
@app.post("/subtract")
def subtract(num1: int, num2: int):

    result = num1 - num2

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


# MULTIPLICATION
@app.post("/multiply")
def multiply(num1: int, num2: int):

    result = num1 * num2

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


# DIVISION
@app.post("/divide")
def divide(num1: int, num2: int):

    if num2 == 0:

        return {
            "message": "Cannot divide by zero"
        }

    result = num1 / num2

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