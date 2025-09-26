# Student Portal - Neon + Render Deployment Guide

This guide will help you deploy the Student Portal to production using Neon PostgreSQL database and Render hosting.

## Prerequisites
- GitHub account
- Neon account and project
- Render account
- Git installed locally

## Step 1: Database Setup (Neon)

1. **Create a Neon account** and log in to [console.neon.tech](https://console.neon.tech)
2. **Create a new project**:
   - Name: `student-portal-db`
   - Region: Choose closest to your location
   - Database: `student_portal`

3. **Get your connection string** from your Neon dashboard
   - Copy the connection string with format:
   ```
   postgresql://username:password@ep-xxx-xxx-xxx.us-east-1.aws.neon.tech/student_portal?sslmode=require
   ```

## Step 2: Database Migration (Local Setup)

1. Copy `env.example` to `.env`:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your Neon database URL:
   ```
   DATABASE_URL=postgresql://your-neon-connection-string-here
   ```

3. Run the migrations locally to set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for production:
   ```bash
   python manage.py createsuperuser
   ```

## Step 3: Render Deployment Setup

1. **Connect to GitHub**:
   - Push your code to a GitHub repository
   - Give Render access to your GitHub account

2. **Deploy via Render Dashboard**:
   
   ### Web Service (Application)
   - **Repository**: Connect your GitHub repo
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ssp.wsgi:application --bind 0.0.0.0:$PORT --timeout 120`
   
   ### Environment Variables for Web Service:
   ```
   SECRET_KEY=<generate-a-new-secret-key>
   DEBUG=False
   DATABASE_URL=<your-neon-connection-string>
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

3. **Alternative: Deploy via render.yaml**:
   - Keep the `render.yaml` file in your repository root
   - In Render dashboard, choose "Deploy a YAML file"
   - Select this repository

## Step 4: Post-Deployment Setup

1. **Run migrations on production**:
   - This happens automatically with the build script
   
2. **Create admin user**:
   ```bash
   python manage.py shell
   ```
   ```python
   from django.contrib.auth import get_user_model
   User = get_user_model()
   User.objects.create_superuser('admin@example.com', 'yourpassword', 'admin', 'yourpassword')
   ```

## Important Production Notes:

### Static Files
- Static files are automatically collected during build process
- They're served via WhiteNoise middleware

### Security
- Ensure `DEBUG=False` in production
- Use HTTPS (Render provides this automatically)
- Keep your `SECRET_KEY` secure
- Use environment variables for all sensitive data

### Performance
- Connection pooling is configured automatically
- Database connection pooling is set to 600 seconds for Neon
- Static file compression is enabled

## Environment Variables Reference:

```bash
# Required for production
SECRET_KEY=your-generated-secret-key
DEBUG=False
DATABASE_URL=postgresql://neon-connection-string
ALLOWED_HOSTS=your-domain.com

# Optional email configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Optional API keys
AVIATIONSTACK_API_KEY=your-api-key
PEXELS_API_KEY=your-api-key
```

## Troubleshooting:

1. **Build failures**: Check build logs in Render dashboard
2. **Database connection**: Verify your Neon connection string
3. **Static files**: Ensure build script runs `collectstatic`
4. **Domain errors**: Update ALLOWED_HOSTS in environment variables

## Monitoring:
- Check Render logs for application performance
- Monitor Neon database performance in their dashboard
- Test all application features post-deployment
