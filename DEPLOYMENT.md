# Deployment Guide - TadiAI

This guide explains how to deploy the standalone FastAPI backend to various hosting platforms.

## ⚡ Quick Deploy to Railway (RECOMMENDED)

Railway is the easiest and fastest way to deploy Flask apps. No complex configuration needed!

### Deploy in 3 Steps

1. **Create Railway Account**: Go to [railway.app](https://railway.app) and sign up with GitHub
2. **New Project**: Click "New Project" → "Deploy from GitHub"
3. **Select Repository**: Choose your TadiAI repository
4. **Add Environment Variable**:
   - Key: `GEMINI_API_KEY`
   - Value: Your actual Gemini API key
5. **Set the start command** if needed: `uvicorn backend:app --host 0.0.0.0 --port $PORT`
6. **Deploy**: Click "Deploy" - done in ~2 minutes!

Your app will be live at: `https://tadiai-production.up.railway.app`

### Why Railway?

✅ One-click GitHub deployment  
✅ Auto-detects Flask from `requirements.txt`  
✅ Free tier with generous limits  
✅ Built for full-stack apps (perfect for Flask)  
✅ Automatic environment variable management  
✅ Instant logs and monitoring  

---

## Alternative: Render

Render is another excellent option with simple deployment.

### Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New Web Service"
4. Select your TadiAI repository

### Configure

| Setting | Value |
| --- | --- |
| Name | tadiai |
| Environment | Python 3 |
| Build Command | (leave empty - auto-detected) |
| Start Command | `python main.py` |
| Instance | Free |

### Add Environment Variable

1. Go to **Environment** tab
2. Add `GEMINI_API_KEY` = your key
3. Deploy!

Your app: `https://tadiai.onrender.com`

---

## Alternative: Heroku

Heroku was a popular choice but now has pricing changes. However, it still works well.

### Deploy to Heroku

```bash
# Install Heroku CLI
# Go to heroku.com and create account

heroku login
heroku create your-app-name
heroku config:set GEMINI_API_KEY=your-key
git push heroku main
heroku open
```

### View Logs

```bash
heroku logs --tail
```

---

## Best platform choice for this project

This app exposes a standalone FastAPI backend with a live API, so it belongs on Python-native hosting. Railway and Render are the simplest options.

**Recommended setup**: Use Railway or Render instead of a static host.

---

## Platform Comparison

| Platform | Best For | Setup Time | Cost | Python Support |
| --- | --- | --- | --- | --- |
| **Railway** | Flask apps | 2 min | Free tier | ✅ Native |
| **Render** | Full-stack | 3 min | Free tier | ✅ Native |
| **Heroku** | All apps | 5 min | Paid | ✅ Native |

---

## Troubleshooting

### App won't start after deployment

**Check logs:**

```bash
# Railway: Dashboard → Logs
# Render: Dashboard → Logs
# Heroku: heroku logs --tail
```

### Common error: "GEMINI_API_KEY is not configured"

**Solution:**

1. Add environment variable in platform dashboard
2. Redeploy the app
3. Check logs to confirm it loaded

### Cold start issues

- Free tier instances sleep after 15 min inactivity
- First request takes 10-30 seconds to respond
- Upgrade to paid tier to avoid this

### API responses are slow

**Solution:**

1. Check Gemini API status at [status.google.com](https://status.google.com)
2. Upgrade your Gemini API plan
3. Check network latency (might be distant server location)

---

## Monitoring Your Deployment

### Railway

- Dashboard shows live metrics
- Logs tab shows all requests and errors
- Deployments tab shows history

### Render

- Dashboard shows uptime
- Logs show all output
- Metrics tab shows performance

### Heroku

```bash
heroku logs --tail                    # Live logs
heroku ps                             # View running processes
heroku config                         # View all variables
```

---

## Auto-Deploy from GitHub

All platforms support automatic deployment:

1. Push code to GitHub
2. Platform automatically redeploys
3. New version is live in 1-2 minutes

No manual deploy commands needed!

---

## Environment Variables Setup

Before deploying, prepare these environment variables:

```env
# Required
GEMINI_API_KEY=your-actual-key-here

# Optional (defaults below)
GEMINI_MODEL=gemini-3.6-flash
PORT=8000
```

Add these in your platform's dashboard under:

- **Railway**: Project → Variables
- **Render**: Environment
- **Heroku**: Settings → Config Vars

---

## Security Best Practices

1. ✅ **Never commit `.env`** - Use platform's secret management
2. ✅ **Rotate API keys** - Change key if accidentally exposed
3. ✅ **Enable HTTPS** - All platforms provide automatic SSL
4. ✅ **Monitor logs** - Check for suspicious activity
5. ✅ **Limit API usage** - Set rate limits if possible

---

## Support & Resources

- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Heroku Docs**: [devcenter.heroku.com](https://devcenter.heroku.com)
- **Flask Deployment**: [flask.palletsprojects.com/deployment](https://flask.palletsprojects.com/deployment)
- **Google Gemini API**: [ai.google.dev](https://ai.google.dev)

---

## Next Steps

1. **Choose a platform** (Railway recommended!)
2. **Create account** and connect GitHub
3. **Add GEMINI_API_KEY** environment variable
4. **Deploy** - your app will be live in minutes!

**Pick Railway and deploy now!** 🚀

---

**Last Updated**: August 2026
