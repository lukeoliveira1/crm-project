from django import forms

from crm.models import Product, Sale, Company

class ProductForm(forms.ModelForm):
    
    class Meta:
      model = Product
      fields = "__all__"
      labels = {
         'name': 'Nome',
         'description': 'Descrição',
         'photo': 'Foto',
         'price': 'Preço',
         'quantity': 'Quantidade',
      }

      widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control'}),
         'description': forms.Textarea(attrs={'class': 'form-control'}),
         'photo': forms.FileInput(attrs={'class': 'form-control'}),
         'price': forms.NumberInput(attrs={'class': 'form-control'}),
         'quantity':forms.NumberInput(attrs={'class': 'form-control'}),
      }

class SaleForm(forms.ModelForm):
   
    class Meta:
      model = Sale
      fields = "__all__"
      labels = {
         'product': 'Produto',
         'quantity_sold': 'Quantidade Vendida',
         'sale_date': 'Data da venda',
      }

      widgets = {
         'product': forms.Select(attrs={'class': 'form-control'}),
         'quantity_sold': forms.NumberInput(attrs={'class': 'form-control'}),
         'sale_date': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
      }
