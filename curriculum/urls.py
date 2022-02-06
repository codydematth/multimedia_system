from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [
    # path('', views.StandardListView.as_view(), name='standard_list'),
    path('', views.SubjectListView.as_view(), name='subject_list'),
    path('<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:slug>/create/', views.LessonCreateView.as_view(),name='lesson_create'),
    path('<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(),name='lesson_detail'),
    path('<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(),name='lesson_update'),
    path('<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(),name='lesson_delete'),

]
