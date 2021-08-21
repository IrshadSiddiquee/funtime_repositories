from django.urls import path
from funtime_guestuser.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]