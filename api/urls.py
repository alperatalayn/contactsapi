from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('contact-list/',views.contactList,name="contact-list"),
    path('pdf-report/',views.pdfReport,name="report"),
    path('create/',views.createContact,name="create"),
    path('update/<str:pk>',views.updateContact,name="update"),
    path('delete/<str:pk>',views.deleteContact,name="delete"),
    path('register/',views.createUser),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
]