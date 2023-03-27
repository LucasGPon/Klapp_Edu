from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include ('home.urls')),
    path('', include ('login.urls')),
    path('', include('alunos.urls')),
    
  
 
]

urlpatterns += [re_path(r'^media/(?P<phat>.*)$',serve,{'document_root': settings.MEDIA_ROOT,}),]