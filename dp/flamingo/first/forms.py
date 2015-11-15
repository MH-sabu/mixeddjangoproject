from django.forms import ModelForm
from first.models import Rating

class RatingForm(ModelForm):
    class Meta:
        model = Rating
