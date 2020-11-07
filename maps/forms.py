from django import forms
from reviews.models import Review


class ReviewCreateSimpleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewCreateSimpleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('created_at', 'store_area', 'checked_number', 'text', 'image2')
        widgets = {
          #  'limit_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
