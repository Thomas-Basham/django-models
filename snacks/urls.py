from django.urls import path

from .views import SnackListView, SnackDetailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail')  # Integer, Primary Key
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
