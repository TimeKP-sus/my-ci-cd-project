# Dự Án CI/CD Pipeline - Chủ Đề 7 (Project Topic 7)

Một cuộc biểu diễn quy trình **Tích Hợp Liên Tục / Triển Khai Liên Tục (CI/CD)** hoàn chỉnh sử dụng GitHub Actions và Render.com.
A complete **Continuous Integration / Continuous Deployment (CI/CD)** pipeline demonstration using GitHub Actions and Render.com.

## 📋 Tổng Quan Dự Án (Project Overview)

Dự án này triển khai một quy trình DevOps đầy đủ tự động hóa vòng đời phát triển phần mềm:
This project implements a full DevOps pipeline that automates the software development lifecycle:
- **Kiểm Soát Phiên Bản**: GitHub (version control) / **Source Control**: GitHub (version control)
- **Xây Dựng**: Cài đặt các phụ thuộc và chuẩn bị ứng dụng / **Build**: Install dependencies and prepare application
- **Kiểm Tra**: Chạy kiểm tra tự động với pytest / **Test**: Run automated tests with pytest
- **Triển Khai**: Triển khai staging tự động, yêu cầu phê duyệt cho production / **Deploy**: Automatic staging, manual approval for production

## 🎯 Yêu Cầu Đáp Ứng (Requirements Met)

✅ **Kiểm Soát Phiên Bản**: Kho GitHub / **Source Control**: GitHub repository  
✅ **Bước Xây Dựng**: Cài đặt các phụ thuộc Python / **Build Step**: Install Python dependencies  
✅ **Bước Kiểm Tra**: Kiểm tra pytest tự động với phạm vi / **Test Step**: Automated pytest testing with coverage  
✅ **Bước Triển Khai**: Triển khai Render.com / **Deploy Step**: Render.com deployment  
✅ **2 Môi Trường**: Staging (tự động) & Production (có phê duyệt) / **2 Environments**: Staging (automatic) & Production (with approval)  
✅ **Phê Duyệt Thủ Công**: Yêu cầu cho triển khai Production / **Manual Approval**: Required for Production deployment  

## 📁 Cấu Trúc Dự Án (Project Structure)

```
my-ci-cd-project/
├── backend/                          # Thư mục Backend - Flask Application
│   ├── app.py                        # Ứng dụng Flask / Flask application
│   ├── requirements.txt              # Các phụ thuộc Python / Python dependencies
│   ├── tests/
│   │   └── test_app.py              # Bài kiểm tra đơn vị (18 test) / Unit tests (18 tests)
│   └── README.md                     # Tài liệu Backend / Backend documentation
├── frontend/                         # Thư mục Frontend - Giao diện Người Dùng
│   └── index.html                   # Trang hạ cánh với thông tin pipeline / Landing page with pipeline info
├── .github/                          # Cấu hình GitHub Actions
│   └── workflows/
│       ├── ci.yml                   # CI Pipeline (Xây Dựng + Kiểm Tra) / CI Pipeline (Build + Test)
│       └── cd.yml                   # CD Pipeline (Triển Khai + Phê Duyệt) / CD Pipeline (Deploy + Approval)
├── render.yaml                       # Cấu hình triển khai Render.com / Render.com deployment config
├── gunicorn_config.py                # Cấu hình máy chủ Gunicorn / Gunicorn configuration
├── .gitignore                        # Các tệp cần bỏ qua Git / Git ignore patterns
└── README.md                         # Tệp này / This file
```

## 🚀 Luồng Pipeline (Pipeline Flow)

```
Push của Lập Trình Viên đến GitHub / Developer Push to GitHub
         │
         ▼
    ┌─────────────────────────┐
    │  Pipeline CI (ci.yml)   │
    │ CI Pipeline (ci.yml)    │
    │  ✓ Checkout code        │
    │  ✓ Thiết lập Python     │
    │  ✓ Cài đặt dep          │
    │  ✓ Chạy kiểm tra        │
    │  ✓ Sinh phạm vi         │
    │  Setup Python           │
    │  ✓ Install deps         │
    │  ✓ Run tests (pytest)   │
    │  ✓ Generate coverage    │
    └─────────────────────────┘
         │
         ├─ Thành Công / Success ──┐
         │                          ▼
         │              ┌──────────────────────┐
         │              │ Triển Khai đến STAGING │
         │              │ Deploy to STAGING      │
         │              │ (Tự động - Không cần   │
         │              │ phê duyệt)             │
         │              │ (Auto - No approval)   │
         │              └──────────────────────┘
         │                        │
         │                        ▼
         │              ┌──────────────────────────────┐
         │              │ Yêu Cầu Phê Duyệt PROD 🔔    │
         │              │ Request PROD Approval        │
         │              │ (Chờ xem xét Thủ Công)       │
         │              │ (Wait for manual review)     │
         │              └──────────────────────────────┘
         │                        │
         │                  ┌─ Phê Duyệt?
         │                  │ Approved?
         │                  │
         │                  ├─ CÓ/YES ──┐
         │                  │           ▼
         │                  │  ┌──────────────────────┐
         │                  │  │ Triển Khai đến PROD  │
         │                  │  │ Deploy to PROD       │
         │                  │  │ (Phê duyệt Thủ Công) │
         │                  │  │ (Manual approval ✓)  │
         │                  │  └──────────────────────┘
         │                  │
         │                  └─ KHÔNG/NO ──┐
         │                                 ▼
         │                            (Dừng - Không triển khai)
         │                            (Stop - Not deployed)
         │
         └─ Lỗi / Failure ──┐
                            ▼
                   (Build failed - No deployment)
```

## 🔧 Technology Stack

| Component | Technology |
|-----------|-----------|
| Runtime | Python 3.11 |
| Framework | Flask 2.3.3 |
| Server | Gunicorn 21.2.0 |
| Testing | pytest 7.4.0 |
| CI/CD | GitHub Actions |
| Deployment | Render.com |
| Version Control | Git + GitHub |

## 📦 Backend Application

### Endpoints

- `GET /` - Main page (HTML interface with pipeline info)
- `GET /health` - Health check endpoint returning JSON
- `GET /api/version` - Version information API

### Running Locally

```bash
# 1. Install dependencies
cd backend
pip install -r requirements.txt

# 2. Run application
python app.py

# 3. Run tests
pytest tests/ -v

# 4. With coverage report
pytest tests/ --cov=. --cov-report=html
```

## 🧪 Testing

The project includes **18 comprehensive unit tests** covering:

```
✓ Health endpoint (returns 200, healthy status)
✓ Index endpoint (returns 200, HTML content)
✓ Version endpoint (returns version info)
✓ Utility functions (add, subtract, multiply)
```

### Run Tests

```bash
cd backend
Môi Trường Triển Khai (Deployment Environments)

### Môi Trường Staging (Staging Environment)
- **Kích Hoạt**: Tự động trên mỗi push đến `main` / **Trigger**: Automatic on every push to `main`
- **Phê Duyệt**: Không yêu cầu / **Approval**: None required
- **URL**: `https://ci-cd-demo-staging.onrender.com`
- **Mục Đích**: Kiểm tra và xác nhận trước production / **Purpose**: Testing and validation before production
- **Gói Render**: Tầng miễn phí / **Render Plan**: Free tier

### Môi Trường Production (Production Environment)
- **Kích Hoạt**: Sau khi triển khai staging thành công / **Trigger**: After staging deployment succeeds
- **Phê Duyệt**: ⚠️ **YÊU CẦU PHÊDUYỆT THỦ CÔNG** trong UI GitHub Actions / **Approval**: ⚠️ **MANUAL APPROVAL REQUIRED** in GitHub Actions UI
- **URL**: `https://ci-cd-demo-production.onrender.com`
- **Mục Đích**: Ứng dụng trực tiếp phục vụ người dùng thực / **Purpose**: Live application serving real users
- **Gói Render**: Gói Starter (có trả phí) /# 🌍 Deployment Environments

### Staging Environment
- **Trigger**: Automatic on every push to `main`
- **Approval**: None required
- **URL**: `https://ci-cd-demo-staging.onrender.com`
- **Purpose**: Testing and validation before production
- **Render Plan**: Free tier

### Production Environment
- **Trigger**: After staging deployment succeeds
- **Approval**: ⚠️ **MANUAL APPROVAL REQUIRED** in GitHub Actions UI
- **URL**: `https://ci-cd-demo-production.onrender.com`
- **Purpose**: Live application serving real users
- **Render Plan**: Starter tier (paid)

## 🔐 GitHub Secrets Required

For deployment to work, add these secrets to your GitHub repository:

1. **`RENDER_API_KEY`**
   - Get from Render.com Dashboard → Account Settings
   - Type: API Token

2. **`STAGING_SERVICE_ID`**
   - From Render.com: Services → Staging service → Copy Service ID
   
3. **`PRODUCTION_SERVICE_ID`**
   - From Render.com: Services → Production service → Copy Service ID

### Add Secrets to GitHub

```
1. Go to: Repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add each secret with its value
4. Click "Add secret"
```

## 📝 Manual Approval Process

**When a push is made to `main`:**

1. CI pipeline runs (build + test)
2. If tests pass, automatic deployment to Staging
3. Notification: Production deployment awaits approval
4. Go to: **Actions** tab → Latest workflow run
5. Click **"Review deployments"**
6. Select `production` environment
7. Click **"Approve and deploy"** or **"Reject"**

## 🔄 Workflow Files

### CI Workflow (`.github/workflows/ci.yml`)
Runs on every push or pull request:
- Python setup
- Dependency installation
- Code linting (flake8)
- Unit tests (pytest)
- Coverage report generation

### CD Workflow (`.github/workflows/cd.yml`)
Runs after successful CI on main branch:
- Deploy to Staging (automatic, no approval)
- Request Production approval
- Deploy to Production (requires manual approval)

## 📊 Monitoring

### Health Checks
Both environments have health check endpoints at `/health`

```bash
curl https://ci-cd-demo-staging.onrender.com/health
```

Response:
```json
{
  "status": "healthy",
  "environment": "staging"
}
```

## 🐛 Troubleshooting

### Pipeline Fails at Test Step
- Check the test output in GitHub Actions → Logs
- Ensure `requirements.txt` has all dependencies
- Run tests locally to debug

### Deployment Fails
- Verify `RENDER_API_KEY` and service IDs are correct
- Check Render.com service logs
- Ensure build command in `render.yaml` is correct

### Manual Approval Not Working
- Confirm GitHub environment `production` exists in Settings → Environments
- Check user has permissions to approve
- Verify deployment is waiting for approval in Actions UI

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Render.com Deployment Guide](https://render.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)

## 🎓 Mục Tiêu Học Tập (Learning Objectives)

Dự án này thể hiện / This project demonstrates:
1. **Khái Niệm CI/CD** - Tự động hóa xây dựng, kiểm tra, triển khai / **CI/CD Concepts** - Automation of build, test, deploy
2. **GitHub Actions** - Tự động hóa quy trình công việc / **GitHub Actions** - Workflow automation
3. **Render.com** - Nền tảng triển khai đám mây / **Render.com** - Cloud deployment platform
4. **Kiểm Tra** - Bài kiểm tra đơn vị với pytest / **Testing** - Unit tests with pytest
5. **Thực Tiễn DevOps Tốt Nhất** - Tách biệt môi trường, phê duyệt thủ công / **DevOps Best Practices** - Environment separation, manual approvals
6. **Phát Triển API** - Xây dựng điểm cuối REST / **API Development** - Building REST endpoints
7. **Kiểm Soát Phiên Bản** - Sử dụng Git/GitHub hiệu quả / **Version Control** - Using Git/GitHub effectively

## ✅ Cách Sử Dụng Dự Án Này (How to Use This Project)

### Để Học Tập (For Learning)
1. Fork kho này / Fork this repository
2. Clone đến máy của bạn / Clone to your machine
3. Đọc code và hiểu từng thành phần / Read the code and understand each component
4. Chạy cục bộ để xem nó hoạt động như thế nào / Run locally to see how it works
5. Triển khai đến Render.com và kích hoạt quy trình / Deploy to Render.com and trigger the pipeline

### Cho Bài Tập Của Bạn (For Your Assignment)
1. Tùy chỉnh ứng dụng (thay đổi tên ứng dụng, thêm tính năng) / Customize the app (change app name, add features)
2. Thêm kiểm tra của riêng bạn / Add your own tests
3. Triển khai đến tài khoản Render.com của bạn / Deploy to your Render.com account
4. Hiển thị quy trình hoạt động cho người hướng dẫn / Show the working pipeline to your instructor

## 📄 License

This project is created for educational purposes as part of Topic 7 CI/CD Pipeline assignment.

---

**Created**: February 2026  
**Status**: ✅ Complete and Ready for Deployment  
**Author**: Student AI Assistant
