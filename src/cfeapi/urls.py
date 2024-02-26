from django.urls import path, include
from django.contrib import admin

# from updates.views import (
#             json_example_view, 
#             JsonCBV, 
#             JsonCBV2, 
#             SerializedDetialView, 
#             SerializedListView
#     )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.api.urls', namespace='api-auth')),
    path('api/user/', include('accounts.api.user.urls', namespace='api-user')),
    path('api/status/', include('status.api.urls', namespace='api-status')),
    path('api/updates/', include('updates.api.urls')), 
]
