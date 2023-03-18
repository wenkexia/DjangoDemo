from django.contrib.auth.models import User
user = User.objects.get(pk=1)
print(user)