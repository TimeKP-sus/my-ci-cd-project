import pytest
from app import app, add, subtract, multiply

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestHealthEndpoint:
    """Tests for health check endpoint"""
    
    def test_health_check_returns_200(self, client):
        """Health endpoint should return 200 status"""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_check_returns_healthy_status(self, client):
        """Health endpoint should return healthy status"""
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] == 'healthy'

class TestIndexEndpoint:
    """Tests for index endpoint"""
    
    def test_index_returns_200(self, client):
        """Index endpoint should return 200 status"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_index_returns_html(self, client):
        """Index endpoint should return HTML content"""
        response = client.get('/')
        assert b'CI/CD Pipeline' in response.data

class TestVersionEndpoint:
    """Tests for version endpoint"""
    
    def test_version_returns_200(self, client):
        """Version endpoint should return 200 status"""
        response = client.get('/api/version')
        assert response.status_code == 200
    
    def test_version_returns_version_info(self, client):
        """Version endpoint should return version information"""
        response = client.get('/api/version')
        data = response.get_json()
        assert data['version'] == '1.0.0'
        assert data['name'] == 'CI/CD Demo App'

class TestUtilityFunctions:
    """Tests for utility functions"""
    
    def test_add_function(self):
        """Test add function"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_subtract_function(self):
        """Test subtract function"""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0
    
    def test_multiply_function(self):
        """Test multiply function"""
        assert multiply(3, 4) == 12
        assert multiply(0, 100) == 0
        assert multiply(-2, 3) == -6
