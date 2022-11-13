
from .req import get
import jwt


JWT_SECRET = 'jwtsecret'


def publicize_user(user):
    return {
        "name": user['name'],
        "username": user['username'],
        "email": user['email'],
        "website": user["website"]
    }


def validate_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET)
        return decoded
    except jwt.DecodeError:
        return None


def get_user_by_email(email, pulbicize=False):
    all_users = get('users')
    for user in all_users:
        if user['email'] == email:
            user['notifications'] = get(f'users/{user["id"]}/todos')
            return (publicize_user(user) if pulbicize else user)
    return None


def authenticate(email, password):
    users_with_email = get(f'users/?email=f{email}')
    for user in users_with_email:
        user_password = user['adress']['zipcode'].split('-')[0]
        if password == user_password:
            token = jwt.encode(user, JWT_SECRET, algorithm="HS256")
            return token
        else:
            return None

            