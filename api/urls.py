from django.urls import path
from . import views

urlpatterns = [
    path('contact-list/',views.contactList,name="contact-list"),
    path('create/',views.createContact,name="create"),
    path('update/<str:pk>',views.updateContact,name="update"),
    path('delete/<str:pk>',views.deleteContact,name="delete")
]