from fastapi import FastAPI
from sympy import sympify

app = FastAPI()


@app.get("/add")
def add(a: float, b: float):
    return a + b


@app.get("/subtract")
def subtract(a: float, b: float):
    return a - b


@app.get("/multiply")
def multiply(a: float, b: float):
    return a * b


@app.get("/division")
def division(a: float, b: float):
    return a / b


@app.get("/calc")
def calc(expr: str):
    result = sympify(expr)
    return {"result": float(result)}




