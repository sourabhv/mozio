from .models import Provider

class ProviderAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = Provider.objects.get(email=username)
            if user.check_password(password):
                return user
        except Provider.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Provider.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except Provider.DoesNotExist:
            return None

