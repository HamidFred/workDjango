from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.rand,name='rand'),
    path('<int:pk>/',views.details,name="detail"),
    
    path('byname/',views.redi_by_name,name="by_name"),
    path('byurl/',views.redi_by_url,name="by_url"),
    path('byobj/',views.redi_by_obj,name="by_obj"),
    path('byview/<int:pk>/',views.redi_by_view,name="by_view"),
]
