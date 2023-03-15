from django.urls import path

from. import views

urlpatterns = [ 
    path("", views.Index, name = "Index"),
    path("details/<int:id>", views.MangaView, name= "MangaView")
]