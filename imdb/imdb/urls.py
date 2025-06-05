from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions

def home(request):
    return HttpResponse("API is running on Render!")

schema_view = get_schema_view(
    openapi.Info(
        title="IMDB API",
        default_version='v1',
        description="API for IMDB clone",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    url="https://imdb-drf-api.onrender.com",  # Must match Render URL exactly
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('imdb_api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Swagger UI
    path('swagger/', csrf_exempt(schema_view.with_ui('swagger', cache_timeout=0)), name='swagger-ui'),
    path('swagger/schema/', csrf_exempt(schema_view.without_ui(cache_timeout=0)), name='swagger-schema'),
]
