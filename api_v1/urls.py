from django.urls import path
from .import views

app_name = 'api_v1'

urlpatterns=[
	path('', views.MailView.as_view(), name="mail-view")
]