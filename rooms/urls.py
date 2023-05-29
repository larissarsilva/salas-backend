from django.urls import path
from .views import ListCreateBlockView, UpdateDeleteBlockView

app_name = 'rooms'

urlpatterns = [
    path('/blocks', ListCreateBlockView.as_view(), name='list-create_blocks'),
    path('/blocks/<int:pk>', UpdateDeleteBlockView.as_view(), name='update-delete_blocks')
]
