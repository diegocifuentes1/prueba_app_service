"""
Main FastAPI application with test endpoints.

This module contains the FastAPI application instance and test routes
for development and testing purposes.
"""

from fastapi import FastAPI
from typing import Dict, Any

# Create FastAPI application instance
app = FastAPI(
    title="Test FastAPI Application",
    description="A simple FastAPI test application with sample endpoints",
    version="1.0.0"
)


def create_test_response() -> Dict[str, Any]:
    """
    Create a test response with sample data.
    
    Returns:
        Dict[str, Any]: A dictionary containing test response data
        
    Example:
        >>> response = create_test_response()
        >>> response["message"]
        "Hello World! This is a test endpoint"
    """
    return {
        "message": "Hello World! This is a test endpoint",
        "status": "success",
        "data": {
            "app_name": "Test FastAPI Application",
            "version": "1.0.0",
            "environment": "development"
        }
    }


@app.get("/")
def read_root() -> Dict[str, Any]:
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        Dict[str, Any]: Welcome message and basic app information
    """
    return create_test_response()


@app.get("/test")
def read_test() -> Dict[str, str]:
    """
    Test endpoint for development purposes.
    
    Returns:
        Dict[str, str]: Simple test response
    """
    return {
        "endpoint": "/test",
        "message": "This is a test endpoint",
        "status": "working"
    }


@app.get("/health")
def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify application status.
    
    Returns:
        Dict[str, str]: Health status information
    """
    return {
        "status": "healthy",
        "service": "FastAPI Test Application"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 