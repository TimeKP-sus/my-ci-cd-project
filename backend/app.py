from flask import Flask, jsonify, send_file
import os
import sys

# Add parent directory to path to serve frontend
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend'), static_url_path='')

@app.route('/')
def index():
    """Root endpoint - Returns frontend dashboard"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend', 'index.html')
    try:
        with open(frontend_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Frontend not found. Running from backend...</h1>", 404

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'environment': os.getenv('ENVIRONMENT', 'development')
    }), 200

@app.route('/api/version')
def version():
    """API endpoint - Returns version info"""
    return jsonify({
        'version': '1.0.0',
        'name': 'CI/CD Demo App',
        'environment': os.getenv('ENVIRONMENT', 'development')
    }), 200

def add(a, b):
    """Utility function for testing"""
    return a + b

def subtract(a, b):
    """Utility function for testing"""
    return a - b

def multiply(a, b):
    """Utility function for testing"""
    return a * b

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
