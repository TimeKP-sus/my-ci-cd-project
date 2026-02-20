# 🚀 Complete Deployment Guide - CI/CD Pipeline

## Overview

This guide walks you through deploying the complete CI/CD pipeline from GitHub to Render.com with manual production approval.

---

## 📋 Prerequisites

- [x] GitHub account (free)
- [x] Render.com account (free signup at https://render.com)
- [x] Code pushed to GitHub (already done: https://github.com/TimeKP-sus/my-ci-cd-project)
- [x] Python 3.13.5 locally (for testing)

---

## ✅ STEP 1: Create Staging Service on Render.com

### 1.1 Go to Render Dashboard
1. Open https://dashboard.render.com
2. Sign up (free tier) if needed
3. Click **"New +"** button (top right)
4. Select **"Web Service"**

### 1.2 Connect GitHub Repository
1. Click **"Build and deploy from a Git repository"**
2. Click **"Connect GitHub"**
3. Authorize Render.com to access your GitHub account
4. Select repository: **`my-ci-cd-project`** (owned by TimeKP-sus)
5. Click **"Connect"**

### 1.3 Configure Staging Service

Fill in these exact values:

| Setting | Value |
|---------|-------|
| **Name** | `ci-cd-demo-staging` |
| **Environment** | `Python 3` |
| **Region** | Choose closest to your location |
| **Branch** | `main` |
| **Build Command** | `pip install -r ./backend/requirements.txt` |
| **Start Command** | `gunicorn -w 4 -b 0.0.0.0:$PORT backend.app:app` |
| **Plan** | `Free` |

### 1.4 Add Environment Variables

1. Click **"Advanced"** (near bottom)
2. Scroll to **"Environment"** section
3. Add these variables:

```
ENVIRONMENT        staging
PYTHON_VERSION     3.13.5
```

### 1.5 Disable Auto-Deploy

⚠️ **IMPORTANT**: Under **"Auto-Deploy"**, select **"No"**

This prevents Render from auto-deploying. GitHub Actions will control deployment instead.

### 1.6 Create the Service

Click **"Create Web Service"** button.

⏳ Wait 5-10 minutes for first deployment. Check logs on the right side.

Once you see: **"Your service is live 🎉"**, proceed to next step.

---

## 📋 STEP 2: Get Staging Service ID

In the Render dashboard:

1. After deployment succeeds, look at the browser URL
2. It will be: `https://dashboard.render.com/web/srv-**xxxxxxxxxxxxx**`
3. Copy the part after `/web/srv-`

**Example**: If URL is `https://dashboard.render.com/web/srv-abc123xyz789`

Then your **STAGING_SERVICE_ID** is: `srv-abc123xyz789`

Save this value - you'll need it shortly.

---

## ✅ STEP 3: Create Production Service on Render.com

**Repeat STEP 1-2**, but with these differences:

### 3.1 Configuration Changes

| Setting | Value |
|---------|-------|
| **Name** | `ci-cd-demo-production` |
| **Plan** | `Starter` (⚠️ **PAID** - ~$7/month) |
| **Environment Variable** | `ENVIRONMENT = production` |

### 3.2 Credit Card Required

When selecting "Starter" plan, you'll need to add a credit card.

**Cost**: ~$7/month for Starter tier (gives you always-on service)

### 3.3 Get Production Service ID

After deployment, repeat Step 2 process.

Your **PRODUCTION_SERVICE_ID** will be different (e.g., `srv-def456uvw012`)

---

## 🔑 STEP 4: Get Render API Key

1. In Render Dashboard, click your **profile icon** (small circle, bottom left)
2. Click **"Account Settings"**
3. Scroll down to **"API Tokens"** section
4. Click **"Create API Token"**
5. Name it: `GitHub-Actions`
6. Copy the long token string
7. **Save it securely** - this is your **RENDER_API_KEY**

Example token: `rnd_abc1234xyz5678...` (very long)

⚠️ **IMPORTANT**: Save this token! You can't view it again after closing.

---

## 🔐 STEP 5: Add GitHub Secrets

Now you have 3 values:
- `RENDER_API_KEY` = (long token from Step 4)
- `STAGING_SERVICE_ID` = `srv-xxxxxxxxxxxxx`
- `PRODUCTION_SERVICE_ID` = `srv-yyyyyyyyyyyyy`

### 5.1 Go to GitHub Secrets

1. Open: https://github.com/TimeKP-sus/my-ci-cd-project/settings/secrets/actions
2. Click **"New repository secret"**

### 5.2 Add RENDER_API_KEY

1. **Name**: `RENDER_API_KEY`
2. **Value**: (paste entire token from Step 4)
3. Click **"Add secret"**

### 5.3 Add STAGING_SERVICE_ID

1. Click **"New repository secret"**
2. **Name**: `STAGING_SERVICE_ID`
3. **Value**: `srv-xxxxxxxxxxxxx` (from Step 2)
4. Click **"Add secret"**

### 5.4 Add PRODUCTION_SERVICE_ID

1. Click **"New repository secret"**
2. **Name**: `PRODUCTION_SERVICE_ID`
3. **Value**: `srv-yyyyyyyyyyyyy` (from Step 3)
4. Click **"Add secret"**

✅ All 3 secrets should now appear in the list.

---

## ⚙️ STEP 6: Configure GitHub Environment (Manual Approval)

This enforces manual approval before production deployment.

### 6.1 Create Environment

1. Go to: https://github.com/TimeKP-sus/my-ci-cd-project/settings/environments
2. Click **"New environment"**
3. Type: `production`
4. Click **"Configure environment"**

### 6.2 Add Required Reviewers

1. Check **"Required reviewers"** ✅
2. Click **"Add approvers"**
3. Select yourself (TimeKP-sus)
4. Click **"Save protection rules"**

✅ Now production deployments MUST be approved by you.

---

## 🧪 STEP 7: Test the Complete Pipeline

Let's trigger the pipeline with a test commit:

```powershell
# Navigate to project
cd d:\DoAnNam4\DIenToan\du_an\my-ci-cd-project

# Make a small change
echo "# Pipeline test" >> backend/app.py

# Commit and push
git add .
git commit -m "Test complete CI/CD pipeline"
git push
```

### 7.1 Watch GitHub Actions

1. Go to: https://github.com/TimeKP-sus/my-ci-cd-project/actions
2. You'll see the workflow running in real-time:

**Stage 1: CI Pipeline**
- ✅ Checkout code
- ✅ Setup Python 3.13
- ✅ Install dependencies (Flask 3.0.0, pytest, gunicorn)
- ✅ Run lint checks
- ✅ Run 18 unit tests
- ✅ Generate coverage reports

**Stage 2: CD Pipeline** (if CI passes)
- ✅ Deploy to Staging (automatic, no approval needed)
- ⏸️ Wait for Production Approval

### 7.2 Approve Production Deployment

1. Still in the Actions tab, click the latest workflow run
2. Wait for it to reach: **"Request Production Approval"** stage
3. Click **"Review deployments"** button
4. Select `production` environment (if multiple)
5. Click **"Approve and deploy"** ✅

⏳ Wait 5-10 minutes for production deployment to complete.

---

## 🌐 STEP 8: Access Your Live Applications

After deployments complete:

### Staging (Always Running)
- **URL**: https://ci-cd-demo-staging.onrender.com
- **Status**: Active (auto-deployed)
- **Health Check**: https://ci-cd-demo-staging.onrender.com/health

### Production (After Approval)
- **URL**: https://ci-cd-demo-production.onrender.com
- **Status**: Active (manually approved)
- **Health Check**: https://ci-cd-demo-production.onrender.com/health

### Test API Endpoints

Visit either URL and click the blue buttons:
- **✓ Check Health** - Test `/health` endpoint
- **📊 Get Version** - Test `/api/version` endpoint

Both should show JSON responses in green.

---

## 📊 Monitoring & Logs

### View Deploy Logs

1. **Render Dashboard**: https://dashboard.render.com
2. Select either service (staging or production)
3. Scroll down to **"Logs"** tab
4. See real-time deployment logs

### View GitHub Actions Logs

1. Go to: https://github.com/TimeKP-sus/my-ci-cd-project/actions
2. Click any workflow run
3. Expand each job to see detailed logs

---

## 🔄 How Continuous Deployment Works

After setup, here's the automatic workflow:

```
1. Developer makes commit
   ↓
2. Push to GitHub
   ↓
3. GitHub Actions triggers CI workflow
   ↓
4. Build → Test (18 tests) → Coverage Report
   ↓
   ├─ Tests PASS ✅
   │  └─ CD Workflow triggered
   │     ├─ Deploy to Staging (automatic)
   │     └─ Request Production Approval ⏸️
   │
   └─ Tests FAIL ❌
      └─ Stop, no deployment (fix code & retry)
   ↓
5. Developer reviews & approves
   ↓
6. Deploy to Production ✅
```

---

## 🆘 Troubleshooting

### Issue: "Could not open requirements file"

**Solution**: Ensure `render.yaml` has correct path:
```yaml
buildCommand: pip install -r ./backend/requirements.txt
```

### Issue: Deployment fails on Render

**Solution**:
1. Check Render service logs
2. Ensure all secrets are added correctly in GitHub
3. Try manual deploy: Render Dashboard → Service → Manual Deploy

### Issue: GitHub Actions fails after manual approval

**Solution**:
1. Verify `RENDER_API_KEY` is correct (not expired)
2. Verify service IDs are correct (not typos)
3. Check Render account has sufficient quota

### Issue: Production approval doesn't appear

**Solution**:
1. Go to Settings → Environments → production
2. Confirm "Required reviewers" is checked
3. Confirm you (TimeKP-sus) is listed as approver

---

## ✅ Deployment Checklist

After completing all steps, verify:

- [ ] Staging service created & deployed
- [ ] Production service created & deployed
- [ ] Render API token obtained
- [ ] 3 GitHub secrets added (RENDER_API_KEY, STAGING_SERVICE_ID, PRODUCTION_SERVICE_ID)
- [ ] GitHub `production` environment configured
- [ ] Test push triggered CI/CD pipeline
- [ ] CI tests passed (18/18)
- [ ] Staging deployed automatically ✅
- [ ] Production approval requested
- [ ] Approved production deployment ✅
- [ ] Both apps live and accessible
- [ ] API endpoints responding with JSON

---

## 📈 Cost Summary

| Component | Cost | Notes |
|-----------|------|-------|
| GitHub | Free | Public repo, unlimited CI/CD minutes |
| Render Staging | Free | Sleeps after 15 min inactivity |
| Render Production | ~$7/month | Always running |
| **Total** | **~$7/month** | Minimal cost for production |

Upgrade Staging to paid plan ($7/month) if you need it always-on.

---

## 🎓 What You've Learned

This project demonstrates:

1. **CI/CD Pipeline Architecture**
   - Automated build, test, deploy workflow
   - Separation of concerns (Build → Test → Deploy)

2. **DevOps Best Practices**
   - Infrastructure as Code (GitHub Actions)
   - Staging/Production separation
   - Manual approval gates
   - Automated testing

3. **Git Workflow**
   - Branch-based deployments
   - Commit triggers automation
   - Code review & approval

4. **Cloud Deployment**
   - PaaS (Render.com)
   - Environment management
   - Health monitoring

5. **Testing & Quality**
   - Automated test suite
   - Code coverage
   - Build validation

---

## 🚀 Next Steps

### To Develop Further

1. Add more tests to improve coverage
2. Add database integration (PostgreSQL on Render)
3. Add environment-specific configurations
4. Add monitoring & alerting
5. Add custom domain names

### To Scale in Production

1. Switch to higher tier on Render
2. Add Redis caching
3. Add error tracking (Sentry)
4. Add performance monitoring (DataDog)
5. Add scheduled backups

---

## 📞 Support

- **GitHub Actions Docs**: https://docs.github.com/en/actions
- **Render Docs**: https://render.com/docs
- **Flask Docs**: https://flask.palletsprojects.com/
- **pytest Docs**: https://docs.pytest.org/

---

**Deployment completed successfully! 🎉**

Your CI/CD pipeline is now fully automated and ready for continuous deployment.

Every time you push code, it will:
1. ✅ Build automatically
2. ✅ Test with 18 unit tests
3. ✅ Deploy to Staging (no approval needed)
4. ⏸️ Wait for your approval to deploy to Production
5. ✅ Deploy to Production (with your approval)

This meets all requirements for **Topic 7: CI/CD Pipeline** assignment! 🚀
