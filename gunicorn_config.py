# ============================================================================
# Tệp Cấu Hình Gunicorn - Cấu hình máy chủ ứng dụng web
# Gunicorn Configuration File - Web Application Server Settings
# ============================================================================

import multiprocessing
import os

# ============================================================================
# Cấu Hình Ổ Cắm Máy Chủ - Server Socket Configuration
# ============================================================================
# Địa chỉ IP và cổng để Gunicorn lắng nghe
bind = "0.0.0.0:%s" % os.environ.get("PORT", 5000)  # Lắng nghe trên tất cả các giao diện, cổng mặc định: 5000
backlog = 2048  # Số lượng kết nối chờ xử lý tối đa

# ============================================================================
# Cấu Hình Tiến Trình Worker - Worker Processes Configuration
# ============================================================================
# Số lượng tiến trình worker xử lý yêu cầu HTTP
workers = max(2, multiprocessing.cpu_count())  # Tối thiểu 2 worker, hoặc bằng số lõi CPU
worker_class = "sync"  # Loại worker: sync = đồng bộ
worker_connections = 1000  # Số kết nối tối đa trên mỗi worker
timeout = 30  # Thời gian chờ tối đa (giây) cho mỗi yêu cầu
keepalive = 2  # Giữ kết nối sống trong bao lâu (giây)

# ============================================================================
# Cơ Chế Máy Chủ - Server Mechanics
# ============================================================================
daemon = False  # Không chạy dưới dạng daemon (chạy ở foreground)
pidfile = None  # Không ghi file PID
umask = 0  # Mặt nạ tệp (0 = không giới hạn)
user = None  # Người dùng chạy process (None = người dùng hiện tại)
group = None  # Nhóm chạy process (None = nhóm hiện tại)
tmp_upload_dir = None  # Thư mục tạm thời để tải lên

# ============================================================================
# Cấu Hình Ứng Dụng - Application Configuration
# ============================================================================
wsgi_app = "backend.app:app"  # Điểm vào ứng dụng WSGI (module.app:variable)
preload_app = False  # Không tải ứng dụng trước khi tạo worker

# ============================================================================
# Cấu Hình Ghi Nhật Ký - Logging Configuration
# ============================================================================
accesslog = "-"  # Ghi nhật ký truy cập (- = stdout)
access_log_format = '%(h)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\"'  # Định dạng nhật ký truy cập
errorlog = "-"  # Ghi nhật ký lỗi (- = stderr)
loglevel = "info"  # Mức độ ghi nhật ký: debug, info, warning, error, critical
