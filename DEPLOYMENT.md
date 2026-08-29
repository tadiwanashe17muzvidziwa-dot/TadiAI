# Deployment Guide - TadiAI

This guide explains how to deploy TadiAI to various hosting platforms.

## Deploying to Netlify

Netlify is the recommended platform for deploying TadiAI as a serverless function-based application.

### Prerequisites

- Netlify account (sign up at [netlify.com](https://netlify.com))
- Git repository (GitHub, GitLab, or Bitbucket)
- Google Gemini API key

### Step 1: Push to Git Repository

```bash
git init
git add .
git commit -m "Initial commit: TadiAI Flask application"
git branch -M main
git remote add origin https://github.com/your-username/TadiAI.git
git push -u origin main
```

### Step 2: Connect Repository to Netlify

1. Go to [Netlify](https://app.netlify.com)
2. Click **"New site from Git"**
3. Choose your Git provider (GitHub, GitLab, Bitbucket)
4. Authorize Netlify to access your repositories
5. Select the **TadiAI** repository
6. Click **"Deploy site"**

### Step 3: Configure Build Settings

Netlify will automatically detect the `netlify.toml` file. The settings are:

- **Base directory**: `/` (root)
- **Build command**: `pip install -r requirements.txt`
- **Functions directory**: `netlify/functions`
- **Publish directory**: `app/templates`

These are pre-configured in `netlify.toml`, so no manual changes needed.

### Step 4: Set Environment Variables

In Netlify Dashboard:

1. Go to **Site settings** → **Build & deploy** → **Environment**
2. Click **"Edit variables"**
3. Add the following environment variables:

| Variable | Value | Required |
|----------|-------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | ✅ Yes |
| `FLASK_ENV` | `production` | Optional |
| `FLASK_DEBUG` | `0` | Optional |

**Important**: Never commit `.env` to Git. Only set variables in Netlify dashboard.

### Step 5: Deploy

Once environment variables are set:

1. Go to **Deploys** tab
2. Click **"Trigger deploy"** → **"Deploy site"**
3. Wait for the build to complete (usually 1-2 minutes)
4. Your site will be live at `https://your-site-name.netlify.app`

### Step 6: Test the Deployment

1. Visit your Netlify URL
2. Try sending a message to TadiAI
3. Check the browser console (F12) for any errors
4. Check Netlify Function logs in dashboard → **Logs**

## Troubleshooting Netlify Deployment

### Issue: "404 Not Found" error

**Solution:**
1. Check `netlify.toml` is in the project root
2. Verify build command ran successfully (check build logs)
3. Ensure `netlify/functions/server.py` exists
4. Clear Netlify cache: **Deploys** → **Trigger deploy** → **Clear cache and deploy**

### Issue: "GEMINI_API_KEY is not configured"

**Solution:**
1. Go to Netlify **Site settings** → **Environment**
2. Verify `GEMINI_API_KEY` variable is set
3. Trigger a new deploy after adding the variable
4. Function logs should now show your API key is configured

### Issue: Function timeout (5+ seconds)

**Solution:**
- Netlify Functions have a 26-second timeout limit (free) or 900 seconds (paid)
- Check if Gemini API is responding slowly
- Try using a different model or API endpoint

### Issue: "python-dotenv not found"

**Solution:**
1. Verify `requirements.txt` includes `python-dotenv==1.1.1`
2. Push changes to Git
3. Trigger a new deploy on Netlify

### Check Logs

Access your deployment logs in Netlify:

1. Go to **Logs** in the Netlify dashboard
2. Select **Functions** tab to see serverless function logs
3. Look for error messages and stack traces
4. Common issues:
   - Missing environment variables
   - Import errors
   - API key issues
   - Network timeouts

## Alternative Deployment Platforms

### Heroku (Traditional Server)

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku config:set GEMINI_API_KEY=your-key
heroku open
```

### Railway (Python-Friendly)

1. Connect GitHub repository at [railway.app](https://railway.app)
2. Add environment variables in project settings
3. Deploy automatically on push

### Render (Easy Deployment)

1. Sign up at [render.com](https://render.com)
2. Create new Web Service from Git
3. Set environment variables
4. Deploy

### PythonAnywhere (Python-Specific)

1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code via Git or direct upload
3. Configure web app settings
4. Set environment variables
5. Reload web app

## Environment Variables Checklist

Before deploying anywhere, ensure you have:

- ✅ `GEMINI_API_KEY` set to your actual API key
- ✅ `.env` file created locally (never commit to Git)
- ✅ All variables in `.env.example` documented
- ✅ No sensitive data in README or code comments
- ✅ `python-dotenv` in `requirements.txt`

## Security Best Practices

1. **Never commit `.env`** - Add to `.gitignore`
2. **Use platform's secret management** - Netlify environment variables, Heroku config vars, etc.
3. **Enable HTTPS** - All platforms support SSL/TLS
4. **Set security headers** - Configured in `netlify.toml`
5. **Monitor function logs** - Check for errors and suspicious activity
6. **Rotate API keys** - Change your Gemini API key if exposed

## Monitoring & Maintenance

### Netlify Dashboard

- **Deploys**: Track deployment history and rollback if needed
- **Logs**: Monitor function execution logs
- **Analytics**: View traffic and performance metrics
- **Settings**: Manage site configuration

### Monitoring Tools

- Set up alerts for deployment failures
- Monitor API usage (Google Cloud Console for Gemini)
- Check error rates in function logs
- Track response times and latency

## Rollback to Previous Version

```bash
# Via Netlify Dashboard
1. Go to Deploys
2. Click on a previous deployment
3. Click "Publish deploy"
```

Or via Git:
```bash
git revert HEAD
git push origin main
# Netlify will auto-deploy the previous version
```

## Custom Domain

1. In Netlify dashboard: **Site settings** → **Domain management**
2. Click **"Add custom domain"**
3. Enter your domain
4. Update DNS records (follow Netlify's instructions)
5. SSL certificate auto-generated

## Performance Optimization

For faster deployments:

1. **Minimize dependencies** - Only install necessary packages
2. **Use Python 3.11+** - Faster execution
3. **Optimize imports** - Load only what you use
4. **Cache static files** - Configure in `netlify.toml`
5. **Monitor function size** - Keep function under 50MB

---

**Need help?** Check:
- [Netlify Docs](https://docs.netlify.com/)
- [Flask Deployment Guide](https://flask.palletsprojects.com/deployment/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
