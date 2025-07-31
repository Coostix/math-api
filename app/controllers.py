from fastapi import APIRouter, Depends, HTTPException, status, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .models import SessionLocal
from .services import pow_op, fibonacci_op, factorial_op, log_request
import functools

router = APIRouter()

API_KEY = "supersecretkey"
def get_api_key(request: Request):
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

class PowRequest(BaseModel):
    x: float
    y: float
class FibRequest(BaseModel):
    n: int
class FactRequest(BaseModel):
    n: int

@functools.lru_cache(maxsize=128)
def cached_fibonacci(n: int):
    return fibonacci_op(n)
@functools.lru_cache(maxsize=128)
def cached_factorial(n: int):
    return factorial_op(n)

@router.post("/pow")
def pow_endpoint(req: PowRequest, db: Session = Depends(SessionLocal), _: str = Depends(get_api_key)):
    result = pow_op(req.x, req.y)
    log_request(db, "pow", f"x={req.x},y={req.y}", result)
    return {"result": result}

@router.post("/fibonacci")
def fibonacci_endpoint(req: FibRequest, db: Session = Depends(SessionLocal), _: str = Depends(get_api_key)):
    result = cached_fibonacci(req.n)
    log_request(db, "fibonacci", f"n={req.n}", result)
    return {"result": result}

@router.post("/factorial")
def factorial_endpoint(req: FactRequest, db: Session = Depends(SessionLocal), _: str = Depends(get_api_key)):
    result = cached_factorial(req.n)
    log_request(db, "factorial", f"n={req.n}", result)
    return {"result": result}

@router.get("/history")
def history_endpoint(db: Session = Depends(SessionLocal), _: str = Depends(get_api_key)):
    logs = db.query(log_request.__annotations__["db"].class_.__table__).all()
    return [dict(row) for row in logs]
