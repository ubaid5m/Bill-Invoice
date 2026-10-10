from django.contrib.auth.forms import UserCreationForm
from .models import customerUser
class customUserCreationform(UserCreationForm):
    class Meta:
        model = customerUser
        fields = ["username","email"]