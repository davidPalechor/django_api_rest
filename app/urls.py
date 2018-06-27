from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('post/', views.CreateInfoView.as_view(), name='create'),
    path('get/', views.InfoListView.as_view(), name='list_info'),
    path('put/', views.UpdateInfoView.as_view(), name='update_info'),
    path('delete/', views.DeleteInfoView.as_view(), name="delete_info")
]
