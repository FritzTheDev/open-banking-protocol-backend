from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/version/<str:api_version>/banks/<str:bank>/', include('account.urls'))
]
