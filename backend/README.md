# Dự Án Demo CI/CD Pipeline - Backend
# CI/CD Pipeline Demo - Backend

Đây là thành phần backend của dự án demo quy trình CI/CD xây dựng bằng Flask.
This is the backend component of the CI/CD pipeline demonstration project built with Flask.

## Tổng Quan (Overview)

Backend cung cấp một ứng dụng Flask đơn giản có các điểm kiểm tra sức khoẻ và API minh họa cách tự động kiểm tra và triển khai hoạt động.
The backend provides a simple Flask application with health checks and APIs that demonstrate how automated testing and deployment work.

## Thiết Lập (Setup)

### Cài Đặt (Installation)

```bash
# Cài đặt các thư viện cần thiết
# Install dependencies
pip install -r requirements.txt
```

### Chạy Ứng Dụng (Running the Application)

```bash
# Chế độ phát triển
# Development mode
python app.py

# Chế độ sản xuất (với gunicorn)
# Production mode (with gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Ứng dụng sẽ có sẵn tại / The application will be available at `http://localhost:5000`

## Các Điểm Cuối API (Endpoints)

- `GET /` - Trang chính với thông tin ứng dụng / Main page with application info
- `GET /health` - Điểm kiểm tra sức khoẻ / Health check endpoint
- `GET /api/version` - Trả về thông tin phiên bản / Returns version information

## Kiểm Tra (Testing)

```bash
# Chạy tất cả các bài kiểm tra
# Run all tests
pytest

# Chạy các bài kiểm tra với báo cáo phạm vi
# Run tests with coverage report
pytest --cov=app tests/

# Chạy tệp kiểm tra cụ thể
# Run specific test file
pytest tests/test_app.py -v
```

## Cấu Trúc Thư Mục (Directory Structure)

```
backend/
├── app.py              # Ứng dụng Flask / Flask application
├── requirements.txt    # Các phụ thuộc Python / Python dependencies
├── tests/
│   └── test_app.py    # Bài kiểm tra đơn vị / Unit tests
└── README.md          # Tệp này / This file
```

## Biến Môi Trường (Environment Variables)

- `PORT` - Số cổng (mặc định: 5000) / Port number (default: 5000)
- `ENVIRONMENT` - Tên môi trường (staging/production) / Environment name (staging/production)

## Quy Trình CI/CD (CI/CD Pipeline)

Ứng dụng này được tự động thực hiện:
This application is automatically:
1. **Biên Dịch** - Cài đặt các phụ thuộc / Built - Dependencies installed
2. **Kiểm Tra** - Chạy bài kiểm tra đơn vị với pytest / Tested - Unit tests run with pytest
3. **Triển Khai** - Đến Render.com Staging (tự động) hoặc Production (phê duyệt thủ công) / Deployed - To Render.com Staging (automatic) or Production (manual approval)

Xem `.github/workflows/` để cấu hình quy trình / See `.github/workflows/` for pipeline configuration.
