class ShopDropDownForm(forms.Form):
    select_shops = forms.ModelChoiceField(queryset=Shop.objects.all(), required=False, label='', empty_label="Show All")