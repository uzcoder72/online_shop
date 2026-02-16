import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()
    email = 'admin@gmail.com'
    password = '123'
    
    if not User.objects.filter(email=email).exists():
        print(f"Creating superuser {email}...")
        User.objects.create_superuser(email=email, password=password)
        print(f"Superuser '{email}' created successfully.")
    else:
        print(f"Superuser '{email}' already exists.")

if __name__ == '__main__':
    create_admin()
