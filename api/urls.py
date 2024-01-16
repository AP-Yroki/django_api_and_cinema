from django.urls import path

from .views import ProductGet

urlpatterns = [
    path('product', ProductGet.as_view()),
    path('products/<int:pk>', ProductGet.as_view()),
    # path('product', ProductGetList.as_view()),
    # path('products/<int:pk>', ProductOne.as_view())
]