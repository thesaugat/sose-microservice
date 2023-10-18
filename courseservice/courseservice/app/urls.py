from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
# from .views import

router = DefaultRouter()

# router.register('books', BooksViewSets, basename="Books")

urlpatterns = [
    path('', include(router.urls)),
    # path('books-borrow/', BooksBorrowViewSets.as_view(), name="Books Borrow"),
]
