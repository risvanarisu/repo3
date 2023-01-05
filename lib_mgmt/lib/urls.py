from django. urls import path
from . import views
urlpatterns = [
    path('hello/',views.registerlibs,name="hy")
]