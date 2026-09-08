# 🔧 Deployment Fix for This Flask App

## The Problem

This project is a Flask application, and the deployment target must support a Python web process.

The main issues are:

- The app runs a Python Flask server from `main.py`
- The API route `/api/chat` requires a live Python backend
- Static-only hosting is not the right fit for this app

If you deploy it to a static-only host, requests to the chat API fail or return 404s.

---

## The Solution: Use a Python Hosting Platform ⚡

Use Railway, Render, or Heroku. These services can run a Flask app and expose the required API routes.

### Deploy Right Now to Railway

1. **Go to**: [railway.app](https://railway.app)
2. **Sign up** with GitHub
3. **Select**: "Deploy from GitHub"
4. **Choose**: Your TadiAI repository
5. **Add environment variables**:
   - `GEMINI_API_KEY` = your actual Gemini API key
   - `GEMINI_MODEL` = `gemini-2.0-flash` (optional but recommended)
   - `PORT` = `5000` (optional if the platform sets it automatically)
6. **Click Deploy**

Your app will be live at a Railway-generated URL such as:
```text
https://your-app.up.railway.app
```

### Why Railway Works

✅ Built for full-stack apps (Flask, Django, etc.)  
✅ Automatically detects and runs Python from `requirements.txt`  
✅ No configuration needed  
✅ Free tier with generous limits  
✅ Auto-deploys when you push to GitHub  
✅ Easy environment variables  
✅ Live logs and monitoring  

---

## Other Options (If You Don't Want Railway)

### Option 2: Render
- [render.com](https://render.com)
- Similar to Railway
- Takes 3 minutes
- Also free tier available

### Option 3: Heroku
- [heroku.com](https://heroku.com)
- Paid only (no free tier anymore)
- Takes 5 minutes
- Good documentation

---

## What NOT To Do

❌ **Don't use a static-only host** for this Flask app  
❌ **Don't try to convert to JavaScript** - too complicated  
❌ **Don't use complex workarounds** - Railway is easier!  

---

## Steps to Deploy to Railway

### 1. Visit Railway

Open [railway.app](https://railway.app) in your browser.

### 2. Create Account (if needed)

Click "Start a New Project" → Sign in with GitHub

### 3. Deploy Repository

- Click "Deploy from GitHub"
- Select your TadiAI repo
- Click "Deploy"

### 4. Add Required Environment Variables

Once deployment starts:
1. Go to **Project** → **Variables**
2. Click **+ New Variable**
3. Add:
   - `GEMINI_API_KEY` = your Gemini API key from [aistudio.google.com](https://aistudio.google.com/app/apikey)
   - `GEMINI_MODEL` = `gemini-2.0-flash` (optional, but recommended)
4. Click **Redeploy Project** (if prompted)

### 5. Get Your Live URL

Once deployed:
- Railway shows your public URL
- Click it to test your app
- Should say "Ask about anything" with the chat box

### 6. Test It Works

1. Type a message: "Hello"
2. Click Send
3. Should get an AI response

---

## Troubleshooting Railway Deployment

### Issue: App won't start
**Check**: Project → Logs tab for error messages

### Issue: "GEMINI_API_KEY not found"
**Fix**:
1. Verify the variable is set in **Variables** tab
2. Redeploy the project
3. Check the logs to confirm the Flask app is loading with the expected environment

### Issue: "Model not found" or invalid Gemini model
**Fix**:
1. Set `GEMINI_MODEL` to `gemini-2.0-flash`
2. Or leave it unset to use the app default
3. Redeploy after changing the variable

### Issue: App is slow
**Normal**: Free tier instances sleep after 15 min. First request takes 10-30 sec. Upgrade to paid to avoid.

### Issue: Can't find deploy button
**Check**: You're logged in? GitHub authorized? Try signing out and back in.

---

## Final Checklist

Before deploying:

- ✅ GitHub repository is up to date
- ✅ `requirements.txt` includes the Flask and Google Gemini dependencies
- ✅ You have a valid Gemini API key
- ✅ The deployment target supports Python web processes
- ✅ You set the required environment variables before launching the app

---

## Questions?

**Railway Support**: [railway.app/support](https://railway.app)  
**Gemini API Help**: [ai.google.dev/docs](https://ai.google.dev/docs)  
**Flask Docs**: [flask.palletsprojects.com](https://flask.palletsprojects.com)

---

## TL;DR - Just Do This

1. Choose a Python hosting platform: Railway, Render, or Heroku
2. Connect the GitHub repository
3. Add `GEMINI_API_KEY` and optionally `GEMINI_MODEL`
4. Deploy the app and test the chat page and API route

🎉 This is the correct setup for a Flask app like TadiAI.
