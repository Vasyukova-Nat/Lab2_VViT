
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

@app.get("/{num1}/{operator}/{num2}/")

def calcu(num1: int, operator: str, num2: int):
    if operator == '+':
        return {num1 + num2}
    elif operator == '-':
        return {num1 - num2}
    elif operator == '*':
        return {num1 * num2}
    elif (operator == ':') and (num2 == 0):
        return {'Ошибка'}
    elif (operator == ':') and (num2 != 0):
        return {num1 / num2}
    elif operator == '^':
        return {num1 ** num2}
    
print('go') #для понимания что код запустился
