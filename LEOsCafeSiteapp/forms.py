from django import forms
from captcha.fields import CaptchaField

class OrderForm(forms.Form):
    boardname = forms.CharField(label="Name", initial='', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardtemperature = forms.ChoiceField(label="Temperature", choices=[('熱', '熱'), ('冰', '冰')], widget=forms.RadioSelect(attrs={'class': 'radio-temp'}), initial='熱', required=True)
    boardcupnumber = forms.IntegerField(label="Cup Number", min_value=1, required=True, widget=forms.NumberInput(attrs={'class': 'orderform-input-text-area'}))
    captcha = CaptchaField()  # Add a CAPTCHA field for spam prevention

class CafeForm(forms.Form):
    boardcbname = forms.CharField(label="Coffee Bean Name", initial='', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardcbcoffeeshop = forms.CharField(label="Coffee Shop", initial='', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardcbplace = forms.CharField(label="Coffee Bean Place", initial='', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardcbroasting = forms.CharField(label="Coffee Bean Roasting", initial='', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardcbprice = forms.CharField(label="Coffee Bean Price", initial='', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardcbflavor = forms.CharField(label="Coffee Bean Flavor", initial='', max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'orderform-input-text-area'}))
    boardcburl = forms.CharField(label="Coffee Bean URL", initial='', max_length=1000, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))
    boardcbcoffeetoday = forms.CharField(label="Coffee Bean Today", initial='', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'orderform-input-text-area'}))