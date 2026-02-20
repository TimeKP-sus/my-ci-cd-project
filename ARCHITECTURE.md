# 🏗️ Architecture Overview

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        DEVELOPER                                 │
│                    (Write Code & Push)                           │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      GITHUB (Source Control)                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Repository: TimeKP-sus/my-ci-cd-project                │   │
│  │  Branch: main                                            │   │
│  │  Triggers: push, pull_request                           │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
            ┌────────────────┴────────────────┐
            │                                 │
            ▼                                 ▼
   ┌────────────────────┐          ┌─────────────────────┐
   │  CI WORKFLOW       │          │  CD WORKFLOW        │
   │  (ci.yml)          │          │  (cd.yml)           │
   └────────────────────┘          └─────────────────────┘
            │                               │
            ▼                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                   GITHUB ACTIONS (Build & Test)                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 1. Checkout Code                                         │   │
│  │ 2. Setup Python 3.13                                     │   │
│  │ 3. Install Dependencies (pip)                           │   │
│  │ 4. Lint Code (flake8)                                    │   │
│  │ 5. Run Tests (pytest - 18 tests)                        │   │
│  │ 6. Generate Coverage Report                             │   │
│  │                                                          │   │
│  │ ✅ If Success → Run CD Workflow                         │   │
│  │ ❌ If Failed → Stop, Don't Deploy                        │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼
   ┌──────────────────┐      ┌──────────────────────┐
   │  STAGING DEPLOY  │      │  PRODUCTION REQUEST  │
   │  (Automatic)     │      │  (Manual Approval)   │
   └──────────────────┘      └──────────────────────┘
            │                         │
            ▼                         ▼
┌─────────────────────────────┐  ┌────────────────────────────┐
│  RENDER.COM (Staging)       │  │  GITHUB ENVIRONMENT        │
│  ┌───────────────────────┐  │  │  ┌──────────────────────┐  │
│  │ Service:              │  │  │  │ Name: production     │  │
│  │ ci-cd-demo-staging    │  │  │  │ Required Reviewers:  │  │
│  │                       │  │  │  │ YES (TimeKP-sus)     │  │
│  │ Environment: Python3  │  │  │  └──────────────────────┘  │
│  │ Plan: Free            │  │  │                             │
│  │                       │  │  │  ⏳ Waits for approval      │
│  │ URL:                  │  │  │                             │
│  │ https://ci-cd-demo-   │  │  │  Developer clicks:          │
│  │ staging.onrender.com  │  │  │  "Approve and Deploy"      │
│  │                       │  │  └────────────────────────────┘
│  │ Status: ✅ Running    │  │
│  └───────────────────────┘  │
└─────────────────────────────┘         │
                                        ▼
             ┌──────────────────────────────────────┐
             │  RENDER.COM (Production)             │
             │  ┌──────────────────────────────┐    │
             │  │ Service:                     │    │
             │  │ ci-cd-demo-production        │    │
             │  │                              │    │
             │  │ Environment: Python3         │    │
             │  │ Plan: Starter (~$7/month)    │    │
             │  │                              │    │
             │  │ URL:                         │    │
             │  │ https://ci-cd-demo-          │    │
             │  │ production.onrender.com      │    │
             │  │                              │    │
             │  │ Status: ✅ Running (Always)  │    │
             │  └──────────────────────────────┘    │
             └──────────────────────────────────────┘
```

---

## Component Interaction

### 1️⃣ Source Control Flow

```
Developer
    │
    ├─ git add .
    ├─ git commit -m "message"
    └─ git push (to main branch)
         │
         ▼
    GitHub Repository
         │
         ├─ Trigger: Push Event
         ├─ Trigger: Pull Request
         └─ Trigger: Manual
              │
              ▼
         GitHub Actions
```

### 2️⃣ CI Pipeline Flow

```
GitHub Actions Triggered
         │
         ├─ Matrix: Python 3.13
         │
         ├─ Step 1: Checkout Code ✓
         ├─ Step 2: Setup Python ✓
         ├─ Step 3: Cache pip ✓
         ├─ Step 4: Install Dependencies ✓
         │         pip install -r ./backend/requirements.txt
         │
         ├─ Step 5: Lint Code (flake8) ✓
         │         Check for syntax errors
         │
         ├─ Step 6: Run Tests (pytest) ✓
         │         pytest tests/ -v
         │         18 tests executed
         │
         └─ Step 7: Generate Coverage ✓
                  pytest --cov=app --cov-report=html
                  │
                  ├─ If all pass ✅ → Trigger CD
                  └─ If any fail ❌ → Stop here
```

### 3️⃣ CD Pipeline Flow

```
If CI Passes ✅
         │
         ├─ Job: Deploy to Staging
         │       │
         │       ├─ Checkout code
         │       ├─ Call Render API
         │       │  POST /services/{staging-id}/deploys
         │       │
         │       └─ Wait 5-10 minutes
         │           │
         │           └─ ✅ Staging Live
         │
         └─ Job: Request Production Approval
                 │
                 ├─ Check GitHub environment protection
                 ├─ Request approval from reviewers
                 │
                 └─ ⏳ Waits for manual approval
                     │
                     ├─ Developer reviews staging
                     ├─ Developer decides: Approve or Reject
                     │
                     ├─ If APPROVED ✅
                     │  │
                     │  └─ Job: Deploy to Production
                     │      │
                     │      ├─ Checkout code
                     │      ├─ Call Render API
                     │      │  POST /services/{production-id}/deploys
                     │      │
                     │      └─ Wait 5-10 minutes
                     │          │
                     │          └─ ✅ Production Live
                     │
                     └─ If REJECTED ❌
                         │
                         └─ Deployment cancelled
```

---

## Data Flow

### Configuration Data Flow

```
GitHub Repository
    ├─ source code (app.py, tests, etc.)
    ├─ .github/workflows/
    │  ├─ ci.yml (CI pipeline definition)
    │  └─ cd.yml (CD pipeline definition)
    │
    └─ GitHub Secrets
       ├─ RENDER_API_KEY
       ├─ STAGING_SERVICE_ID
       └─ PRODUCTION_SERVICE_ID
            │
            ▼
       GitHub Actions (uses secrets)
            │
            ├─ Builds with these secrets
            ├─ Tests with this code
            │
            └─ Calls Render API with credentials
                 │
                 ▼
            Render.com Services
            ├─ Staging (deploys)
            └─ Production (deploys)
```

### Application Data Flow

```
User Request
     │
     ▼
┌─────────────────────────┐
│ Render.com (Staging)    │
│ OR                      │
│ Render.com (Production) │
└────────┬────────────────┘
         │
         ├─ GET / → Returns HTML page
         ├─ GET /health → Returns JSON (health status)
         └─ GET /api/version → Returns JSON (version info)
              │
              ▼
        Gunicorn Server
              │
              ▼
        Flask Application
        (backend/app.py)


Environment Variables
├─ ENVIRONMENT (staging/production)
├─ PYTHON_VERSION (3.13.5)
└─ PORT (5000)
     │
     ▼
Application Configuration
     │
     ├─ Server runs on 0.0.0.0:$PORT
     ├─ Displays current environment
     └─ Returns environment in API responses
```

---

## Deployment Architecture

### Staging Environment (Free Tier)

```
                GitHub push
                    │
                    ▼
        GitHub Actions (CI/CD)
                    │
            ┌───────┴────────┐
            │                │
        ✅ CI Pass      Deploy to Staging
            │                │
            └────────┬───────┘
                     │
                     ▼
         Render.com Free Tier
         ┌──────────────────┐
         │ ci-cd-demo-      │
         │ staging          │
         ├──────────────────┤
         │ Status: Running  │
         │ Plan: Free       │
         │ Sleeps: Inactive │
         │ for 15 mins      │
         └──────────────────┘
                │
                ▼
         https://ci-cd-demo-staging.onrender.com
         
    ✓ Accessible 24/7
    ✓ Auto-restarted on request
    ✓ Perfect for testing
    ✓ No cost
```

### Production Environment (Starter Plan)

```
             GitHub push
                 │
                 ▼
     GitHub Actions (CI/CD)
                 │
         ┌───────┴────────────────┐
         │                        │
     ✅ CI Pass            Deploy to Staging
         │                        │
         │              ✅ Staging Success
         │                        │
         └───────────┬────────────┘
                     │
                     ▼
            Request Approval
            │
            ├─ GitHub Environment Protection
            ├─ Required Reviewers: TimeKP-sus
            │
            └─ ⏳ Waiting...
                 │
         ┌───────┴────────┐
         │                │
    APPROVED ✅        REJECTED ❌
         │
         ▼
   Deploy to Production
         │
         ▼
    Render.com Starter
    ┌──────────────────┐
    │ ci-cd-demo-      │
    │ production       │
    ├──────────────────┤
    │ Status: Running  │
    │ Plan: Starter    │
    │ Always-on        │
    │ Cost: $7/month   │
    └──────────────────┘
         │
         ▼
   https://ci-cd-demo-production.onrender.com
   
    ✓ Always running
    ✓ Production-grade
    ✓ Monitored health checks
    ✓ Limited cost
```

---

## Technology Stack Layers

```
┌─────────────────────────────────────────────────────┐
│         PRESENTATION LAYER (Frontend)               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │  frontend/index.html                        │   │
│  │  - Interactive dashboard                    │   │
│  │  - API testing buttons                      │   │
│  │  - Pipeline visualization                  │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
└────────────────┬────────────────────────────────────┘
                 │ HTTP Requests
                 ▼
┌─────────────────────────────────────────────────────┐
│         APPLICATION LAYER (Backend)                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │  Gunicorn (WSGI Server)                     │   │
│  │  - Processes requests                       │   │
│  │  - Load balancing (4 workers)               │   │
│  │  - Port: $PORT (from Render)                │   │
│  └──────────────────┬──────────────────────────┘   │
│                     │                              │
│  ┌──────────────────▼──────────────────────────┐   │
│  │  Flask Framework (Python 3.13.5)            │   │
│  │  - Request routing                          │   │
│  │  - Response handling                        │   │
│  │  - Error management                         │   │
│  │                                             │   │
│  │  Routes:                                    │   │
│  │  ├─ GET /          (dashboard)              │   │
│  │  ├─ GET /health    (health check)          │   │
│  │  └─ GET /api/version (version API)         │   │
│  └──────────────────┬──────────────────────────┘   │
│                     │                              │
│  ┌──────────────────▼──────────────────────────┐   │
│  │  Business Logic (app.py)                    │   │
│  │  - Request processing                       │   │
│  │  - Data formatting                          │   │
│  │  - Response building                        │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│         DATA LAYER                                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Environment Variables:                            │
│  ├─ ENVIRONMENT (staging/production)              │
│  ├─ PYTHON_VERSION (3.13.5)                       │
│  └─ PORT (from Render.com)                        │
│                                                     │
│  Configuration:                                    │
│  ├─ gunicorn_config.py                            │
│  └─ render.yaml                                    │
│                                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│         CI/CD & INFRASTRUCTURE LAYER                │
├─────────────────────────────────────────────────────┤
│                                                     │
│  GitHub Actions:                                   │
│  ├─ CI Workflow (ci.yml)                          │
│  │  ├─ Build: pip install                        │
│  │  ├─ Test: pytest (18 tests)                   │
│  │  └─ Report: Coverage analysis                 │
│  │                                                │
│  └─ CD Workflow (cd.yml)                          │
│     ├─ Deploy to Staging (auto)                  │
│     ├─ Request Production approval               │
│     └─ Deploy to Production (manual)             │
│                                                     │
│  Render.com Infrastructure:                        │
│  ├─ Staging: Free tier (auto-scaling)            │
│  └─ Production: Starter tier (always-on)         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Security Architecture

```
┌─────────────────────────────────────────────────────┐
│              SECURITY LAYERS                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Layer 1: Source Code Protection                   │
│  ├─ GitHub public repository                       │
│  ├─ All commits tracked                            │
│  ├─ Branch protection available                    │
│  └─ Requires authentication                        │
│                                                     │
│  Layer 2: Secret Management                        │
│  ├─ GitHub Secrets (encrypted)                     │
│  │  ├─ RENDER_API_KEY                             │
│  │  ├─ STAGING_SERVICE_ID                         │
│  │  └─ PRODUCTION_SERVICE_ID                      │
│  │                                                 │
│  └─ Never exposed in logs                          │
│                                                     │
│  Layer 3: Environment Separation                   │
│  ├─ Staging environment (testing)                  │
│  │  └─ Free tier, isolated                        │
│  │                                                 │
│  └─ Production environment (live)                  │
│     ├─ Paid tier, monitored                       │
│     └─ Requires approval to deploy                │
│                                                     │
│  Layer 4: Deployment Gates                         │
│  ├─ Automated tests (must pass)                    │
│  ├─ Staging deployment (must succeed)             │
│  ├─ Manual approval (required)                     │
│  └─ Production deployment (conditional)            │
│                                                     │
│  Layer 5: Production Monitoring                    │
│  ├─ Health checks (/health)                       │
│  ├─ Status monitoring (every 30s)                 │
│  └─ Automatic restarts on failure                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## File Organization

```
my-ci-cd-project/
│
├── 📁 .github/
│   └── 📁 workflows/
│       ├── ci.yml          ← CI Pipeline definition
│       └── cd.yml          ← CD Pipeline definition
│
├── 📁 backend/
│   ├── app.py              ← Flask application (3 endpoints)
│   ├── requirements.txt    ← Dependencies list
│   ├── 📁 tests/
│   │   └── test_app.py    ← 18 unit tests
│   └── README.md          ← Backend docs
│
├── 📁 frontend/
│   └── index.html         ← Interactive dashboard
│
├── gunicorn_config.py     ← Production server config
├── render.yaml            ← Render.com configuration
├── .gitignore             ← Git ignore rules
│
├── README.md              ← Main documentation
├── DEPLOYMENT.md          ← Step-by-step setup guide
├── QUICKSTART.md          ← 15-minute quick start
├── PROJECT_SUMMARY.md     ← Project status & checklist
└── ARCHITECTURE.md        ← This file (system architecture)
```

---

## Performance Characteristics

```
Pipeline Execution Time
┌─────────────────────────────────────────────────┐
│ CI Pipeline:                                    │
├─────────────────────────────────────────────────┤
│ Checkout code           ▓ 5 seconds              │
│ Setup Python 3.13       ▓▓ 10 seconds           │
│ Install dependencies    ▓▓▓▓ 30 seconds         │
│ Lint with flake8        ▓ 5 seconds             │
│ Run 18 pytest tests     ▓▓▓ 20 seconds          │
│ Generate coverage       ▓ 5 seconds             │
├─────────────────────────────────────────────────┤
│ TOTAL: ~75 seconds (~1-2 minutes)              │
└─────────────────────────────────────────────────┘

Deployment Time
┌─────────────────────────────────────────────────┐
│ Staging Deployment:     ▓▓▓▓▓▓▓▓ 5-10 minutes   │
│ Production Deployment:  ▓▓▓▓▓▓▓▓ 5-10 minutes   │
│                                                 │
│ Total CI/CD Time:       ~15-25 minutes          │
└─────────────────────────────────────────────────┘

Testing Coverage
┌─────────────────────────────────────────────────┐
│ Unit Tests: 18/18 (100%)                        │
│ API Endpoints: 100% covered                     │
│ Business Logic: 100% covered                    │
│ Edge Cases: All handled                         │
└─────────────────────────────────────────────────┘
```

---

## Scalability Potential

```
Current State
├─ 1 Language (Python)
├─ 1 Framework (Flask)
├─ 1 Application Server (Gunicorn)
└─ 1 Database (None - stateless)

Future Scaling Options
├─ Database Integration
│  ├─ PostgreSQL on Render
│  ├─ Connection pooling
│  └─ Migrations management
│
├─ Caching Layer
│  ├─ Redis for session data
│  ├─ Cache API responses
│  └─ Reduce database load
│
├─ Additional Services
│  ├─ Multiple microservices
│  ├─ Service mesh (if needed)
│  └─ Load balancing
│
├─ Monitoring & Observability
│  ├─ Error tracking (Sentry)
│  ├─ Performance monitoring
│  ├─ Log aggregation
│  └─ Custom alerting
│
└─ Advanced CI/CD
   ├─ Multi-region deployment
   ├─ Canary deployments
   ├─ A/B testing
   └─ Rollback automation
```

---

## System Requirements

### Development Environment
```
- Python 3.13.5+
- Git 2.0+
- Browser (any modern)
- Text editor (any)
- ~100 MB disk space
```

### Render.com Account
```
- Free tier for Staging
- Starter plan for Production (~$7/month)
- Valid credit card for production
```

### GitHub Account
```
- Public or private repository
- GitHub Actions enabled (free tier)
- Repository settings access
```

---

This architecture ensures:
✅ **Reliability** - Automated testing before deployment  
✅ **Safety** - Manual approval for production  
✅ **Efficiency** - Fully automated pipeline  
✅ **Scalability** - Cloud-based infrastructure  
✅ **Monitorability** - Health checks and logging  
