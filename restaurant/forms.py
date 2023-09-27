from django import forms
from restaurant.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("created_at", "updated_at", "slug")

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields['name_and_surname'].widget.attrs.update({"placeholder": "Your name and surname"})
        self.fields['subject'].widget.attrs.update({"placeholder": "Subject"})
        self.fields['message'].widget.attrs.update({"placeholder": "Your message", "style": "height:150px"})
        self.fields['email'].widget.attrs.update({"placeholder": "Your email"})

