from django.urls import path
from . import views
app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<int:pk>', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:review_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:review_pk>/comments/<int:comment_pk>/recomments/',views.recomments_create, name='recomments_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/recomments/<int:recomment:pk>/delete/',views.recomments_delete, name='recomments_delete'),
    path('short/', views.shortreview_list, name='shortreview_list'),
    path('shortcreate/', views.shortcreate, name='shortcreate'),
    path('short/<int:short_pk>/', views.shortdetail, name='shortdetail'),
    path('short/<int:short_pk>/update/', views.shortupdate, name='shortupdate'),
    path('short/<int:short_pk>/delete/',views.shortdelete, name='shortdelete'),
    path('report/', views.report, name='report'),
    path('report/<int:pk>/resolve/', views.report_to_content, name='report_to_content'),
    path('report/new/<str:sort>/<int:pk>', views.report_create, name='report_create')

]