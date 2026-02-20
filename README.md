# CI/CD Pipeline Project - Topic 7

A complete **Continuous Integration / Continuous Deployment (CI/CD)** pipeline demonstration using GitHub Actions and Render.com.

## 📋 Project Overview

This project implements a full DevOps pipeline that automates the software development lifecycle:
- **Source Control**: GitHub (version control)
- **Build**: Install dependencies and prepare application
- **Test**: Run automated tests with pytest
- **Deploy**: Automatic staging, manual approval for production

## 🎯 Requirements Met

✅ **Source Control**: GitHub repository  
✅ **Build Step**: Install Python dependencies  
✅ **Test Step**: Automated pytest testing with coverage  
✅ **Deploy Step**: Render.com deployment  
✅ **2 Environments**: Staging (automatic) & Production (with approval)  
✅ **Manual Approval**: Required for Production deployment  

## 📁 Project Structure

```
my-ci-cd-project/
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── tests/
│   │   └── test_app.py    # Unit tests (18 tests)
│   └── README.md          # Backend documentation
├── frontend/
│   └── index.html         # Landing page with pipeline info
├── .github/
│   └── workflows/
│       ├── ci.yml         # CI Pipeline (Build + Test)
│       └── cd.yml         # CD Pipeline (Deploy + Approval)
├── render.yaml            # Render.com deployment config
├── .gitignore             # Git ignore patterns
└── README.md              # This file
```

## 🚀 Pipeline Flow

```
Developer Push to GitHub
         │
         ▼
    ┌─────────────────────────┐
    │   CI Pipeline (ci.yml)  │
    │  ✓ Checkout code        │
    │  ✓ Setup Python         │
    │  ✓ Install deps         │
    │  ✓ Run tests (pytest)   │
    │  ✓ Generate coverage    │
    └─────────────────────────┘
         │
         ├─ Success ──┐
         │            ▼
         │      ┌──────────────────────┐
         │      │ Deploy to STAGING    │
         │      │ (Auto - No approval) │
         │      └──────────────────────┘
         │            │
         │            ▼
         │      ┌──────────────────────────────┐
         │      │ Request PROD Approval 🔔     │
         │      │ (Wait for manual review)     │
         │      └──────────────────────────────┘
         │            │
         │      ┌─ Approved?
         │      │    │
         │      │    ├─ YES ──┐
         │      │    │        ▼
         │      │    │  ┌──────────────────────┐
         │      │    │  │ Deploy to PROD       │
         │      │    │  | (Manual approval ✓)  │
         │      │    │  └──────────────────────┘
         │      │    │
         │      │    └─ NO ──┐
         │      │             ▼
         │      │        (Stop - Not deployed)
         │
         └─ Failure ──┐
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

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=app tests/

# Run specific test file
pytest tests/test_app.py -v
```

## 🌍 Deployment Environments

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

## 🎓 Learning Objectives

This project demonstrates:
1. **CI/CD Concepts** - Automation of build, test, deploy
2. **GitHub Actions** - Workflow automation
3. **Render.com** - Cloud deployment platform
4. **Testing** - Unit tests with pytest
5. **DevOps Best Practices** - Environment separation, manual approvals
6. **API Development** - Building REST endpoints
7. **Version Control** - Using Git/GitHub effectively

## ✅ How to Use This Project

### For Learning
1. Fork this repository
2. Clone to your machine
3. Read the code and understand each component
4. Run locally to see how it works
5. Deploy to Render.com and trigger the pipeline

### For Your Assignment
1. Customize the app (change app name, add features)
2. Add your own tests
3. Deploy to your Render.com account
4. Show the working pipeline to your instructor

## 📄 License

This project is created for educational purposes as part of Topic 7 CI/CD Pipeline assignment.

---

**Created**: February 2026  
**Status**: ✅ Complete and Ready for Deployment  
**Author**: Student AI Assistant
