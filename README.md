# Student Portal (SSP) - Django Web Application

A comprehensive student portal built with Django that provides various educational tools and utilities for students.

## 🚀 Features

### Core Functionality
- **User Authentication**: Secure registration and login system
- **Notes Management**: Create, view, and delete personal notes
- **Homework Tracker**: Manage assignments with due dates and completion status
- **Todo List**: Simple task management system
- **User Profile**: Dashboard showing pending homework and todos

### Educational Tools
- **YouTube Search**: Search and discover educational videos
- **Book Search**: Find books using Google Books API
- **Dictionary**: Look up word definitions, pronunciations, and examples
- **Wikipedia Search**: Quick access to Wikipedia articles
- **Unit Conversion**: Convert between different units (length, mass)

### Technical Features
- **Responsive Design**: Bootstrap 4 powered UI
- **Crispy Forms**: Beautiful form rendering
- **User-specific Data**: All data is tied to individual user accounts
- **Production Ready**: Configured for deployment with security best practices

## 🛠️ Technology Stack

- **Backend**: Django 5.1.6
- **Frontend**: HTML, CSS, Bootstrap 4
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Django's built-in user authentication
- **Forms**: Django Crispy Forms with Bootstrap 4
- **Static Files**: WhiteNoise for serving static files
- **Deployment**: Vercel-ready configuration

## 📋 Prerequisites

- Python 3.12+
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd student_portal
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Copy the example environment file and configure your settings:
```bash
cp env.example .env
```

Edit `.env` file with your configuration:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## 🌐 Deployment on Vercel

### Prerequisites for Vercel Deployment
- Vercel account
- GitHub repository with your code

### Deployment Steps

1. **Prepare Environment Variables**
   Set the following environment variables in your Vercel dashboard:
   ```
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-domain.vercel.app,localhost
   DATABASE_URL=your-production-database-url
   ```

2. **Deploy to Vercel**
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Login to Vercel
   vercel login
   
   # Deploy
   vercel
   ```

3. **Database Configuration**
   For production, consider using:
   - **Vercel Postgres**: Built-in PostgreSQL service
   - **PlanetScale**: MySQL-compatible database
   - **Supabase**: PostgreSQL with additional features

### Vercel Configuration Files
The project includes:
- `vercel.json`: Vercel deployment configuration
- `wsgi.py`: WSGI entry point for Vercel
- `runtime.txt`: Python version specification

## 📁 Project Structure

```
student_portal/
├── dashboard/                 # Main Django app
│   ├── migrations/           # Database migrations
│   ├── templates/           # HTML templates
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   └── urls.py              # URL patterns
├── ssp/                     # Django project settings
│   ├── settings.py          # Main settings file
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── static/                  # Static files (CSS, images)
├── staticfiles/             # Collected static files
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel deployment config
├── wsgi.py                 # Vercel WSGI entry point
├── runtime.txt             # Python version
└── manage.py               # Django management script
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `DATABASE_URL` | Database connection URL | `sqlite:///db.sqlite3` |
| `EMAIL_HOST` | SMTP server host | `smtp.gmail.com` |
| `EMAIL_PORT` | SMTP server port | `587` |
| `EMAIL_USE_TLS` | Use TLS for email | `True` |
| `EMAIL_HOST_USER` | Email username | Empty |
| `EMAIL_HOST_PASSWORD` | Email password | Empty |

### Security Features
- CSRF protection enabled
- XSS protection headers
- Secure cookie settings
- HSTS headers for HTTPS
- Content type sniffing protection

## 🎯 Usage

### Getting Started
1. Register a new account or login
2. Navigate through the different sections using the sidebar
3. Create notes, add homework, and manage todos
4. Use the educational tools for research and learning

### Key Features Usage

#### Notes Management
- Click "Notes" to view all your notes
- Click "Add Note" to create a new note
- Click on a note title to view details
- Use "Delete" button to remove notes

#### Homework Tracker
- Add homework with subject, title, description, and due date
- Mark homework as completed by clicking the checkbox
- Delete homework entries when no longer needed

#### Educational Tools
- **YouTube**: Search for educational videos
- **Books**: Find books using Google Books API
- **Dictionary**: Look up word definitions
- **Wikipedia**: Search Wikipedia articles
- **Conversion**: Convert between different units

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure `DATABASE_URL` is correctly set
   - Run migrations: `python manage.py migrate`

2. **Static Files Not Loading**
   - Collect static files: `python manage.py collectstatic`
   - Check `STATIC_ROOT` and `STATIC_URL` settings

3. **Email Configuration Issues**
   - Verify email credentials in `.env`
   - Check SMTP server settings

4. **Vercel Deployment Issues**
   - Ensure all environment variables are set
   - Check `vercel.json` configuration
   - Verify Python version in `runtime.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as a student project for educational purposes.

## 🔗 External APIs Used

- **Google Books API**: For book search functionality
- **Dictionary API**: For word definitions
- **Wikipedia API**: For article search
- **YouTube Search API**: For video search

## 📞 Support

For support and questions, please open an issue in the GitHub repository.

---

**Note**: This application is designed for educational purposes. Make sure to comply with the terms of service of external APIs used in the application.
