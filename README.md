# Math API

A microservice for mathematical operations (power, Fibonacci, factorial) with a REST API and CLI, built using FastAPI, SQLAlchemy, and Docker.

## Features

- **REST API** for mathematical operations:
  - Power (`/pow`)
  - Fibonacci (`/fibonacci`)
  - Factorial (`/factorial`)
  - Request history (`/history`)
- **API Key authentication** via `x-api-key` header
- **Request logging** to a SQLite database
- **CLI** for local operations
- **Dockerized** for easy deployment

## Getting Started

### Prerequisites

- Python 3.11+
- [pip](https://pip.pypa.io/)
- [Docker](https://www.docker.com/) 

### Installation

1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt

### With Uvicorn

uvicorn app.main:app --reload

### With Docker

docker build -t math-api .
docker run -p 8000:8000 math-api

### API Usage
POST /pow
Body: { "x": 2, "y": 8 }
POST /fibonacci
Body: { "n": 10 }
POST /factorial
Body: { "n": 5 }
GET /history
Returns all logged requests

Interactive docs: http://localhost:8000/docs

### CLI Usage
**Activate your virtual environment first:**
Power: python cli.py pow --base 2 --exponent 8 OR python cli.py pow -b 2 -e 8
Fibonacci: python cli.py fib --n 10
Factorial: python cli.py fact --n 5