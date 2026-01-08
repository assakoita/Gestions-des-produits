from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help_text for all fields to avoid verbose messages in the UI
        for field in self.fields.values():
            field.help_text = None
