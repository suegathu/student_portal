import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ssp.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def handler(request):
    return application(request)
