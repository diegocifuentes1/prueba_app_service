# Test FastAPI Application

A simple FastAPI test application with sample endpoints for development and testing purposes.

## Features

- **Root endpoint** (`/`): Returns a welcome message with app information
- **Test endpoint** (`/test`): Simple test endpoint for development
- **Health check** (`/health`): Health status verification

## Installation

### Option 1: Using requirements.txt (Recommended)
```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### Option 2: Using pyproject.toml
```bash
# Install production dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

## Running the Application

### Option 1: Using the project script
```bash
start
```

### Option 2: Using uvicorn directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 3: Running the Python file directly
```bash
python main.py
```

## API Endpoints

Once the application is running, you can access:

- **Root**: http://localhost:8000/
- **Test endpoint**: http://localhost:8000/test
- **Health check**: http://localhost:8000/health
- **API Documentation**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## Development

The application is configured with:
- **Black** for code formatting
- **Ruff** for linting
- **Pytest** for testing

## Project Structure

```
prueba_app_service/
├── main.py              # FastAPI application
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # Development dependencies
└── README.md            # Project documentation
``` 