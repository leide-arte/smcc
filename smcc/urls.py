
from django.contrib import admin
from django.urls import path, include
from apps.aluno import urls as aluno_urls
from apps.home import urls as home_urls
from apps.disciplinas import urls as disciplinas_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(home_urls), name='home'),
    
    path('aluno/', include(aluno_urls), name='aluno'),

    path('disciplinas/', include(disciplinas_urls), name='disciplinas'),
]
