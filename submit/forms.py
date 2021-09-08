from django import forms


class SubmitForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    email = forms.CharField(max_length=255, required=False)
    author = forms.CharField(label="", max_length=255, required=True)
    title = forms.CharField(label="Your story's title",
                            max_length=255, required=True)
    story = forms.CharField(label="Your story", widget=forms.Textarea)
    avatar = forms.CharField(label="", max_length=255, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'e.g. https://getavataaars.com/?accessoriesType=Prescription01&avatarStyle=Transparent&eyeType=Happy&mouthType=Default&topType=LongHairFroBand'}))
