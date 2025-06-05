
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt 

def home(request):
    return HttpResponse("API is running on Render!")

schema_view = get_schema_view(
    openapi.Info(
        title="IMDB API",
        default_version='v1',
        description="API for IMDB clone",
    ),
    public=True
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/',
         include([
             path('', include('imdb_api.urls')),
             path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

            # Exempt CSRF for Swagger UI
             path(
                 'swagger/schema',
                 csrf_exempt(schema_view.with_ui('swagger', cache_timeout=0)),
                 name='schema-swagger-ui'
             ),
         ]))
]
