
from django.contrib import admin
from django.urls import path
from hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name ='home'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctor, name='doctor'),
    path('appointments/', views.appointment, name='appointment'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

]

