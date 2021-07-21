from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name="ui_utils"
urlpatterns = [
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    # path('error404/', views.error_404,name='error_404'),
    # path('error500/', views.error_500,name='error_500'),
    # path('downtime/', views.error_downtime,name='error_downtime'),
    # path('browser-compactability/', views.error_browser,name='error_browser'),
    # path('', views.index,name='index'),
    # path('privacy/', views.privacy,name='privacy'),
    # path('termsofuse/', views.termsofuse,name='termsofuse'),
    # path('disclamier/', views.disclaimer,name='disclaimer'),
    # path('ajax-wrapper/',views.ajax_wrapper.as_view(),name='ajax_wrapper'),
    # path('ajax-wrapper/<str:method>/',views.ajax_wrapper.as_view(),name='ajax_wrapper'),

]
