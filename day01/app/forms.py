from django import forms
from .models import Supplier,Order,Employee,Category,Unit,Item

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__' 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'