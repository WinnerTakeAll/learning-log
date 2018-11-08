from django.urls import path
from . import views

app_name = 'learning'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
]