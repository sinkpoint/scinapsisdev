from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def login_action(self):
        login = self.cleaned_data['username']
        passw = self.cleaned_data['password']

class SearchFilterForm(forms.Form):
    target_human = forms.BooleanField(label="human")
    target_mouse = forms.BooleanField(label="mouse")
    t = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, queryset, *args, **kwargs):
        super(SearchFilterForm, self).__init__(*args, **kwargs)
        suppliers = queryset.values('supplier').annotate()
        com = [('','Company')]+[(s['supplier'],s['supplier']) for s in suppliers]
        self.fields['company'] = forms.ChoiceField(choices=com)

        hosts = queryset.values('prod__host').annotate()
        ho = [('','Hosts')]+[(h['prod__host'],h['prod__host']) for h in hosts]
        self.fields['host'] = forms.ChoiceField(choices=ho)

