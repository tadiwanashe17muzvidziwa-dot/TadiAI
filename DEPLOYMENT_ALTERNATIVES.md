# Railway Deployment Guide

Railway is the easiest way to deploy TadiAI. It has:

- ✅ Native Python support
- ✅ Automatic environment variables
- ✅ Easy scaling
- ✅ Free tier available

## Quick Deploy to Railway

### Step 1: Connect GitHub to Railway

1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub"
4. Authorize Railway to access your GitHub
5. Select your TadiAI repository

### Step 2: Configure Environment

1. Railway will detect `requirements.txt`
2. Add environment variables:
   - Go to **Project** → **Variables**
   - Add: `GEMINI_API_KEY=your-key-here`
   - Add: `FLASK_ENV=production`

### Step 3: Deploy

Railway will automatically:

- Install dependencies from `requirements.txt`
- Run your Flask app on port 5000
- Assign a public URL (e.g., `https://tadiai-production.up.railway.app`)

**That's it!** No additional configuration needed.

## Using Railway CLI (Optional)

```bash
npm install -g @railway/cli
railway login
railway link
railway up
```

## Monitoring

- View logs: Railway dashboard → Logs tab
- Check status: Dashboard shows deployment status
- Scale: Project settings → Instance size

---

## Render Deployment Guide

Render is another excellent option with simple Python support.

## Quick Deploy to Render

### Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +"
4. Select "Web Service"
5. Select your TadiAI repository

### Step 2: Configure Settings

| Setting | Value |
| --- | --- |
| Name | tadiai |
| Environment | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python main.py` |
| Instance Type | Free |

### Step 3: Add Environment Variables

1. Go to **Environment** tab
2. Add:
   - Key: `GEMINI_API_KEY`
   - Value: `your-actual-key`
3. Click "Deploy"

### Step 4: Monitor Deployment

- Deployment logs appear in real-time
- Once complete, your app is live at `https://tadiai.onrender.com`
- Logs tab shows runtime errors

## Auto-Deploy

Render automatically redeploys when you push to GitHub!

---

## Heroku Deployment Guide (Legacy but Simple)

Heroku requires a Procfile but works well for Flask apps.

## Setup

### Step 1: Create Procfile

```bash
# Create file: Procfile (no extension)
```

Add to `Procfile`:

```text
web: python main.py
```

### Step 2: Update requirements.txt

Add gunicorn for production:

```bash
pip install gunicorn
pip freeze > requirements.txt
```

Update Procfile:

```text
web: gunicorn app:app
```

### Step 3: Deploy to Heroku

```bash
heroku login
heroku create your-app-name
heroku config:set GEMINI_API_KEY=your-key
git push heroku main
heroku open
```

### Step 4: View Logs

```bash
heroku logs --tail
```

---

## Comparison

| Platform | Ease | Cost | Python Support | Best For |
| --- | --- | --- | --- | --- |
| **Railway** | ⭐⭐⭐⭐⭐ | Free tier | ✅ Native | **Recommended** |
| **Render** | ⭐⭐⭐⭐ | Free tier | ✅ Native | Good alternative |
| **Heroku** | ⭐⭐⭐ | Paid only | ✅ Native | Legacy option |

---

## Recommended: Deploy to Railway RIGHT NOW

1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub"
4. Select your TadiAI repo
5. Add `GEMINI_API_KEY` environment variable
6. Click Deploy - **Done in 2 minutes!**

Your TadiAI will be live with a URL like: `https://tadiai-production.up.railway.app`

---

## Best fit for this app

This project is a Flask application, so it performs best on Python-native hosting providers such as Railway or Render.

**Switch to Railway today!** It's the fastest path and works cleanly with Flask. 🚀
