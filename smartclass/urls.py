from django.contrib import admin
from django.urls import path, include

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('account/', include('account.urls')),
    path('', views.index, name="index")
]
