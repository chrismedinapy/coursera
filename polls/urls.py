from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='polls'),
    path('polls', views.index, name='polls2'),
    path('polls/owner', views.owner, name='owner'),
    # path('polls', views.owner, name='polls'),
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail2'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]