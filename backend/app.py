# ============================================================================
# CI/CD DEMO APP - Backend Flask Application (Ứng dụng Backend Flask)
# ============================================================================

from flask import Flask, jsonify, send_file
import os
import sys

# Thêm thư mục cha vào đường dẫn để phục vụ frontend
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Khởi tạo ứng dụng Flask và cấu hình thư mục tĩnh (frontend)
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend'), static_url_path='')

@app.route('/')
def index():
    """
    Điểm cuối (Endpoint) gốc - Trả về dashboard frontend
    Hàm này phục vụ trang HTML chính của ứng dụng
    """
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend', 'index.html')
    try:
        # Mở và đọc file index.html
        with open(frontend_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # Nếu file không tìm thấy, trả về lỗi 404
        return "<h1>Frontend không tìm thấy. Đang chạy từ backend...</h1>", 404
@app.route('/hieucube')
def hieucube():
    return jsonify(
        {
            'chim:': '3,6cm',
            'ket qua danh gia': 'chim be vl'
        }
    ), 200

@app.route('/health')
def health():
    """
    Điểm cuối kiểm tra sức khỏe (Health Check)
    Trả về trạng thái của ứng dụng và môi trường hiện tại
    """
    return jsonify({
        'status': 'healthy',  # Trạng thái: khỏe mạnh
        'environment': os.getenv('ENVIRONMENT', 'development')  # Môi trường: development hoặc production
    }), 200  # Mã trạng thái HTTP 200 (OK)

@app.route('/api/version')
def version():
    """
    Điểm cuối API - Trả về thông tin phiên bản
    Cung cấp thông tin về phiên bản ứng dụng và môi trường
    """
    return jsonify({
        'version': '1.0.0',  # Phiên bản ứng dụng
        'name': 'CI/CD Demo App',  # Tên ứng dụng
        'environment': os.getenv('ENVIRONMENT', 'development')  # Môi trường hiện tại
    }), 200  # Mã trạng thái HTTP 200 (OK)

# ============================================================================
# Các hàm tiện ích để kiểm tra (Utility Functions for Testing)
# ============================================================================

def add(a, b):
    """
    Hàm cộng hai số
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    Returns:
        Tổng của a và b
    """
    return a + b

def subtract(a, b):
    """
    Hàm trừ hai số
    Args:
        a: Số bị trừ
        b: Số trừ
    Returns:
        Hiệu của a và b
    """
    return a - b

def multiply(a, b):
    """
    Hàm nhân hai số
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    Returns:
        Tích của a và b
    """
    return a * b

# ============================================================================
# Điểm vào chính của ứng dụng (Main Entry Point)
# ============================================================================
if __name__ == '__main__':
    # Lấy cổng từ biến môi trường, mặc định là 5000
    port = int(os.getenv('PORT', 5000))
    # Chạy máy chủ Flask
    # debug=True: Cho phép tải lại tự động khi code thay đổi
    # host='0.0.0.0': Lắng nghe trên tất cả các giao diện mạng
    app.run(debug=True, host='0.0.0.0', port=port)
