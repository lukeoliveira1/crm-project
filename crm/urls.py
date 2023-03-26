
from django.urls import path
from crm.views import index, products, product_by_id, create_product, edit_product, sales, sale_by_id, create_sale, edit_sale

urlpatterns = [
   path('', index, name='index'),
   path('products', products, name='products'),
   path('products/<int:product_id>', product_by_id, name='product_by_id'),
   path('create_product', create_product, name='create_product'),
   path('edit_product', edit_product, name='edit_product'),
   path('sales', sales, name='sales'),
   path('sales/<int:sale_id>', sale_by_id, name='sale_by_id'),
   path('create_sale', create_sale, name='create_sale'),
   path('edit_sale', edit_sale, name='edit_sale'),
]
