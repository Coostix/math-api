from sqlalchemy.orm import Session
from .models import RequestLog
import logging

logger = logging.getLogger("math_api_service")

def pow_op(x: float, y: float) -> float:
    return x ** y

def fibonacci_op(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial_op(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def log_request(db: Session, operation: str, input_data: str, result: float):
    log = RequestLog(operation=operation, input_data=input_data, result=result)
    db.add(log)
    db.commit()
    db.refresh(log)
    logger.info(f"Logged {operation}: {input_data} -> {result}")
    return log
