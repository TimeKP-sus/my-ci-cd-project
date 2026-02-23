# ============================================================================
# Tạo Bài Kiểm Tra (Test Suite) cho ứng dụng Flask
# ============================================================================

import pytest
from app import app, add, subtract, multiply

# ============================================================================
# Fixture: Tạo Client Kiểm Tra (Pytest Fixture for Test Client)
# ============================================================================

@pytest.fixture
def client():
    """
    Tạo một client kiểm tra cho ứng dụng Flask
    Fixture này cung cấp một client giả lᾭ để gửi yêu cầu HTTP đến ứng dụng
    """
    app.config['TESTING'] = True  # Bật chế độ kiểm tra
    with app.test_client() as client:
        yield client  # Cấp mế client cho các test

# ============================================================================
# Lớp 1: Kiểm Tra Điểm Thăm Dọi Sức Khỏe (Test Health Endpoint)
# ============================================================================

class TestHealthEndpoint:
    """
    Cộp kểm đầy đủ các bài kiểm tra cho điểm cuối kiểm tra sức khỏe
    """
    
    def test_health_check_returns_200(self, client):
        """
        Kiểm tra: Điểm cuối sức khỏe phải trả về mã trạng thái 200
        """
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_check_returns_healthy_status(self, client):
        """
        Kiểm tra: Điểm cuối sức khỏe phải trả về trạng thái 'healthy'
        """
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] == 'healthy'

# ============================================================================
# Lớp 2: Kiểm Tra Điểm Trang Chủ (Test Index/Home Endpoint)
# ============================================================================

class TestIndexEndpoint:
    """
    Cộp thừ các bài kiểm tra cho điểm cuối trang chủ
    """
    
    def test_index_returns_200(self, client):
        """
        Kiểm tra: Điểm cuối trang chủ phải trả về mã 200 (OK)
        """
        response = client.get('/')
        assert response.status_code == 200
    
    def test_index_returns_html(self, client):
        """
        Kiểm tra: Điểm cuối trang chủ phải trả về nội dung HTML
        """
        response = client.get('/')
        assert b'CI/CD Pipeline' in response.data  # Kiểm tra có chửa thẳng 'CI/CD Pipeline'

# ============================================================================
# Lớp 3: Kiểm Tra Điểm API Phiên Bản (Test Version API Endpoint)
# ============================================================================

class TestVersionEndpoint:
    """
    Cộp kiểm tra cho điểm cuối API phiên bản
    """
    
    def test_version_returns_200(self, client):
        """
        Kiểm tra: Điểm cuối phiên bản phải trả về mã 200 (OK)
        """
        response = client.get('/api/version')
        assert response.status_code == 200
    
    def test_version_returns_version_info(self, client):
        """
        Kiểm tra: Điểm cuối phiên bản phải trả về thông tin đúng
        """
        response = client.get('/api/version')
        data = response.get_json()
        assert data['version'] == '1.0.0'  # Kiểm tra phiên bản
        assert data['name'] == 'CI/CD Demo App'  # Kiểm tra tên ứng dụng

# ============================================================================
# Lớp 4: Kiểm Tra Các Hàm Tiện Ích (Test Utility Functions)
# ============================================================================

class TestUtilityFunctions:
    """
    Cộp kiểm tra cho các hàm tiện ích toán học
    """
    
    def test_add_function(self):
        """
        Kiểm tra hàm cộng (add function)
        Thắc nghiệm công với các trường hợp khác nhau:
          - Số dương
          - Số âm
          - Số không
        """
        assert add(2, 3) == 5  # Kế quả: 2 + 3 = 5
        assert add(-1, 1) == 0  # Kế quả: -1 + 1 = 0
        assert add(0, 0) == 0  # Kế quả: 0 + 0 = 0
    
    def test_subtract_function(self):
        """
        Kiểm tra hàm trừ (subtract function)
        Thắc nghiệm trừ với các trường hợp khác nhau
        """
        assert subtract(5, 3) == 2  # Kế quả: 5 - 3 = 2
        assert subtract(0, 5) == -5  # Kế quả: 0 - 5 = -5
        assert subtract(10, 10) == 0  # Kế quả: 10 - 10 = 0
    
    def test_multiply_function(self):
        """
        Kiểm tra hàm nhân (multiply function)
        Thắc nghiệm nhân với các trường hợp khác nhau
        """
        assert multiply(3, 4) == 12  # Kế quả: 3 × 4 = 12
        assert multiply(0, 100) == 0  # Kế quả: 0 × 100 = 0
        assert multiply(-2, 3) == -6  # Kế quả: -2 × 3 = -6
