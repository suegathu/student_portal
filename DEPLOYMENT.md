# Deployment Guide for Student Portal

## Quick Deploy to Vercel

### 1. Prerequisites
- GitHub account
- Vercel account (free tier available)
- Your code pushed to GitHub

### 2. Deploy Steps

1. **Connect GitHub to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/login with GitHub
   - Click "New Project"
   - Import your GitHub repository

2. **Configure Environment Variables**
   In Vercel dashboard, go to Settings → Environment Variables and add:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.vercel.app
   DATABASE_URL=sqlite:///db.sqlite3
   ```

3. **Deploy**
   - Click "Deploy" button
   - Wait for deployment to complete
   - Your app will be available at `https://your-app-name.vercel.app`

### 3. Database Setup (Optional)
For production, consider using:
- **Vercel Postgres** (recommended)
- **PlanetScale** (MySQL)
- **Supabase** (PostgreSQL)

### 4. Custom Domain (Optional)
- Go to Settings → Domains
- Add your custom domain
- Follow DNS configuration instructions

## Local Development

```bash
# Clone repository
git clone <your-repo-url>
cd student_portal

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp env.example .env
# Edit .env with your settings

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Troubleshooting

### Common Issues:
1. **Build fails**: Check Python version in `runtime.txt`
2. **Static files not loading**: Run `python manage.py collectstatic`
3. **Database errors**: Verify `DATABASE_URL` environment variable
4. **Import errors**: Check all dependencies in `requirements.txt`

### Support:
- Check Vercel logs in dashboard
- Review Django logs in application
- Ensure all environment variables are set correctly
