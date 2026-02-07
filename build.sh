#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

cd backend
python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='gikonyo').exists():
    User.objects.create_superuser('gikonyo', 'gikonyo.mwema@gmail.com', 'Gikonyo!')
    print('Superuser created')
"
