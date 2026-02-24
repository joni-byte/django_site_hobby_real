import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.contrib.auth.models import User

# შეცვალე 'admin' და 'newpassword123' შენი სასურველი მონაცემებით
username = 'admin'
new_password = 'Jonathan123#'

user = User.objects.filter(username=username).first()
if user:
    user.set_password(new_password)
    user.save()
    print(f"Password for {username} updated successfully!")
else:
    User.objects.create_superuser(username, 'admin@example.com', new_password)
    print(f"Superuser {username} created successfully!")