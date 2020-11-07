from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('created_at',)
        widgets = {
            'limit_date': forms.DateInput(attrs={'class':'datepicker'}),
        }