from django.urls import path
from .views import CategoryListEndpoint, AddCategoryEndpoint, ProductEndpoint

urlpatterns = [
    path('categories', CategoryListEndpoint.as_view(), name="category"),
    path('add/category', AddCategoryEndpoint.as_view(), name='add_cate'),
    path('product', ProductEndpoint.as_view(), name='product'),


]