# 🚀 Quick Start Guide

**Thời gian**: 15 phút để hoàn thành  
**Level**: Beginner friendly

---

## 📋 Quick Checklist (Làm tuần tự)

### ✅ 1. Prepare Render.com (5 min)

1. Go to https://render.com → Sign up (free)
2. Create **Staging service**:
   - Name: `ci-cd-demo-staging`
   - Plan: Free
   - Build: `pip install -r ./backend/requirements.txt`
   - Start: `gunicorn -w 4 -b 0.0.0.0:$PORT backend.app:app`
   - Env vars: `ENVIRONMENT=staging`, `PYTHON_VERSION=3.13.5`
   - Wait for "live" ✅
   - Copy Service ID: `srv-xxxxx...`

3. Create **Production service**:
   - Name: `ci-cd-demo-production`
   - Plan: Starter ($7/month)
   - Same build/start commands & env vars (change ENVIRONMENT to production)
   - Copy Service ID: `srv-yyyyy...`

4. Get **API Token**:
   - Settings → API Tokens → Create Token
   - Copy token: `rnd_abc123...`

### ✅ 2. Configure GitHub (5 min)

1. Go to Settings → Secrets and variables → Actions
2. Add 3 secrets:
   ```
   RENDER_API_KEY          = rnd_abc123...
   STAGING_SERVICE_ID      = srv-xxxxx...
   PRODUCTION_SERVICE_ID   = srv-yyyyy...
   ```

3. Go to Settings → Environments
4. Create `production` environment
5. Check "Required reviewers" → Add yourself

### ✅ 3. Test Pipeline (5 min)

```powershell
cd my-ci-cd-project
git commit --allow-empty -m "Test pipeline"
git push
```

Watch at: https://github.com/TimeKP-sus/my-ci-cd-project/actions

- ✅ CI runs (tests pass)
- ✅ Deploy to Staging (automatic)
- ⏸️ Wait for Production approval

Click "Review deployments" → Approve → ✅ Deploy to Production

---

## 🌐 Your Live Apps

- **Staging**: https://ci-cd-demo-staging.onrender.com
- **Production**: https://ci-cd-demo-production.onrender.com

Test the blue buttons on either website!

---

## ❓ Common Issues

| Problem | Solution |
|---------|----------|
| File not found | Add `./` to path: `./backend/requirements.txt` |
| Secret not working | Check spelling - secrets are case-sensitive |
| Approval doesn't appear | Environment `production` must exist |
| No auto-deploy to production | That's correct - manual approval required! |

---

## 📚 Full Details

For detailed step-by-step guide, see [DEPLOYMENT.md](DEPLOYMENT.md)

---

**Done! Your CI/CD is live! 🎉**
