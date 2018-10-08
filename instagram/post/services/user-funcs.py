from django.contrib.auth.models import User

def create_user(username, first_name, last_name, email):
    mi_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
    mi_user.save()

def get_users():
    return User.objects.all()

def get_user(username, email):
    get_user = User.objects.filter(username=username, email=email)
    if get_user.count() > 0:
        return get_user[0]
    return None