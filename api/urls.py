from django.urls import path
from . import views

urlpatterns = [
    path('contact-list/',views.contactList,name="contact-list"),
    path('create/',views.createContact,name="create"),
    path('update/<str:input>',views.updateContact,name="update"),
    path('delete/<str:input>',views.deleteContact,name="delete")
]