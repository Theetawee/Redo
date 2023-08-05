from collections.abc import Callable, Iterable, Mapping
from typing import Any
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
import threading



class EmailThread(threading.Thread):
    def __init__(self, email):
        threading.Thread.__init__(self)
        self.email = email  # Set the email attribute

    def run(self):
        self.email.send()

        
        
        
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        value =six.text_type(str(user.pk))+six.text_type(str(timestamp))+six.text_type(user.verified_email)
        return value
        
generate_token=TokenGenerator()






def send_activation_email(user, request):
    token = generate_token.make_token(user)
    current_site = get_current_site(request)
    email_subject = 'Account activation'
    email_body = render_to_string('accounts/verification.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token,
        'lead': settings.ACCOUNT_PROTOCOL
    })
    email = EmailMessage(email_subject, email_body, from_email=settings.EMAIL_HOST_USER, to=[user.email])
    
    EmailThread(email).start()

