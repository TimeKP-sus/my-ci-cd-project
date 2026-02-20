# CI/CD Pipeline Demo - Backend

This is the backend component of the CI/CD pipeline demonstration project built with Flask.

## Overview

The backend provides a simple Flask application with health checks and APIs that demonstrate how automated testing and deployment work.

## Setup

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Development mode
python app.py

# Production mode (with gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

The application will be available at `http://localhost:5000`

## Endpoints

- `GET /` - Main page with application info
- `GET /health` - Health check endpoint
- `GET /api/version` - Returns version information

## Testing

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=app tests/

# Run specific test file
pytest tests/test_app.py -v
```

## Directory Structure

```
backend/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── tests/
│   └── test_app.py    # Unit tests
└── README.md          # This file
```

## Environment Variables

- `PORT` - Port number (default: 5000)
- `ENVIRONMENT` - Environment name (staging/production)

## CI/CD Pipeline

This application is automatically:
1. **Built** - Dependencies installed
2. **Tested** - Unit tests run with pytest
3. **Deployed** - To Render.com Staging (automatic) or Production (manual approval)

See `.github/workflows/` for pipeline configuration.
