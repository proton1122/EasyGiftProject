from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
 
 
class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
 
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', )
 
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomerRegisterForm(forms.Form):

    customer_name = forms.CharField(label= "名前")
    customer_zipcode = forms.CharField(label="郵便番号")
    customer_prefecture = forms.CharField(label="都道府県")
    customer_city = forms.CharField(label="市区町村")
    customer_address1 = forms.CharField(label="丁目・番地など")
    customer_address2 = forms.CharField(label="建物名など")
    customer_tel = forms.CharField(label="電話番号")
    customer_mail = forms.EmailField(label="メールアドレス")