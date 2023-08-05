from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist

UserModel = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the given username is an email address
            user = UserModel.objects.get(email=username)
        except ObjectDoesNotExist:
            try:
                # If the username is not an email, try with the username field
                user = UserModel.objects.get(username=username)
            except ObjectDoesNotExist:
                try:
                    # If the username is not a username, try with the phone field
                    user = UserModel.objects.get(phone=username)
                except ObjectDoesNotExist:
                    return None  # User with given email/username/phone does not exist
                else:
                    if user.check_password(password):
                        return user
            else:
                if user.check_password(password):
                    return user
        else:
            if user.check_password(password):
                return user
