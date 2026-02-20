from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Root endpoint - Returns simple HTML page"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Pipeline Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
            }
            .container {
                background: #f4f4f4;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 { color: #333; }
            .status { color: #27ae60; font-weight: bold; }
            .env { background: #ecf0f1; padding: 10px; border-radius: 4px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Pipeline Demo</h1>
            <p>This application is deployed via GitHub Actions to Render.com</p>
            <div class="status">✓ Application is running successfully</div>
            <div class="env">
                <strong>Environment:</strong> """ + os.getenv('ENVIRONMENT', 'development') + """
            </div>
            <div class="env">
                <strong>Version:</strong> 1.0.0
            </div>
            <p><small>Last updated: """ + str(__import__('datetime').datetime.now()) + """</small></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

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
