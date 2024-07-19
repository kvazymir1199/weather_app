from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(
        max_length=100,
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search'})
    )
