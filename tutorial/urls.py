from django.urls import path
from . import views

urlpatterns = [
    path('<pagename>/', views.topic, name='topic'),
    path('<pagename>/<title_post>', views.post_detail, name='post_detail'),
]

